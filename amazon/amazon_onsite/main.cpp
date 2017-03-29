//
//  main.cpp
//  Amazon
//
//  Created by Hawsang on 11/30/16.
//  Copyright © 2016 LeightonSt. All rights reserved.
//

#include "misc.h"
#include "data.h"

typedef struct picosts {
    ProductInventory* _piptr;
    vector<ShippingCost> _vsc;
    
    picosts (ProductInventory &pi_) : _piptr (&pi_) {};
} Picosts;

typedef struct shipping_plan {
    Order _order;
    vector<picosts> _costs;
    
    shipping_plan (const Order &order_) : _order (order_) {};
} ShippingPlan;

void myprint (const ShippingPlan &src) {
    cout << "Order: " << src._order.getPid() << endl;
    for (Picosts pit : src._costs) {
        if (pit._piptr->getRegion() == north) cout << '\t' << "Region: North" << endl;
        else cout << '\t' << "Region: Unknown" << endl;
        for (ShippingCost scit : pit._vsc) {
            cout << '\t' << '\t' << "Cost: "<< scit.getDays() << " " << scit.getCost() << endl;
        }
    }
}

void myprint (const ProductInventory *piptr, int num, int time) {
    cout << piptr->getPid() << " shipped: " << num << " remains: " << piptr->getQuantity() << endl;
    cout << "Used time " << time << endl;
}

ShippingPlan solution1 (Order order) {
    ShippingPlan sp (order);
    int pid = order.getPid();
    Region region_to = order.getDestination();
        
    for (ProductInventory& piit : pis) {
        Picosts pic (piit);
        if (piit.getPid() == pid) {
            Region region_from = piit.getRegion();
            for (ShippingCost scit : scs) {
                if (scit.getShipFrom() == region_from && scit.getShipTo() == region_to) {
                    pic._vsc.push_back(scit);
                }
            }
        }
        if (pic._vsc.size()) sp._costs.push_back(pic);
    }
    return sp;
}

struct orderComparator {
    bool operator () (const Order &order1, const Order &order2) {
        return order1.getQuantity() < order2.getQuantity();
    }
} OrderComparator;

typedef pair<ProductInventory*, int> InventoryMincost;

struct inventoryPairComparator {
    bool operator () (const InventoryMincost& ip1, const InventoryMincost& ip2) {
        return ip1.second < ip2.second;
    }
} InventoryPairComparator;

void solution2 () {
    vector<Order> data (orders);
    sort(data.begin(), data.end(), OrderComparator);
    
    for (Order oit : data) {
        priority_queue<InventoryMincost, vector<InventoryMincost>, inventoryPairComparator> pq;
        ShippingPlan plan = solution1(oit);
        if (plan._costs.empty()) continue;
        
        int sum_of_product = 0;
        for (Picosts& pcit : plan._costs) {
            if (pcit._vsc.empty()) continue;
            
            int min_days = INT_MAX;
            for (ShippingCost scit : pcit._vsc) {
                if (scit.getDays() < min_days) min_days = scit.getDays();
            }
            InventoryMincost imc;
            imc.first = pcit._piptr;
            imc.second = min_days;
            
            if (pcit._piptr->getQuantity()) pq.push(imc);
            sum_of_product += pcit._piptr->getQuantity();
        }
        
        if (sum_of_product < oit.getQuantity()) continue;
        int to_be_sent = oit.getQuantity();
        
        while (to_be_sent > 0 && !pq.empty()) {
            InventoryMincost headim = pq.top();
            pq.pop();
            
            int sent_num = min(to_be_sent, headim.first->getQuantity());
            to_be_sent -= sent_num;
            headim.first->reduceQuantity(sent_num);
            myprint(headim.first, sent_num, headim.second);
        }
    }
}

int main(int argc, const char * argv[]) {
    std::cout << "Hello, World!\n";
    for (Order oit : orders) myprint(solution1(oit));
    solution2();
    return 0;
}
