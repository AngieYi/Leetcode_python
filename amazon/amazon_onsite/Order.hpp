//
//  Order.hpp
//  Amazon
//
//  Created by Hawsang on 11/30/16.
//  Copyright © 2016 LeightonSt. All rights reserved.
//

#ifndef Order_hpp
#define Order_hpp

#include "misc.h"

class Order {
private:
    int _pid;
    int _quantity;
    int _expected_days;
    Region _region;
    double _date;
    
public:
    Order (int pid_, int quantity_, int expected_days_, Region region_, double date_) :
    _pid (pid_),
    _quantity (quantity_),
    _expected_days (expected_days_),
    _region (region_),
    _date (date_) {};
    
    Order (const Order &other_) {
        _pid = other_._pid;
        _quantity = other_._quantity;
        _expected_days = other_._expected_days;
        _region = other_._region;
        _date = other_._date;
    }
    
    const int getPid () const { return _pid; }
    const int getQuantity () const { return _quantity; }
    const Region getDestination () const { return _region; }
};

#endif /* Order_hpp */
