//
//  ProductInventory.hpp
//  Amazon
//
//  Created by Hawsang on 11/30/16.
//  Copyright © 2016 LeightonSt. All rights reserved.
//

#ifndef ProductInventory_hpp
#define ProductInventory_hpp

#include "misc.h"

class ProductInventory {
private:
    int _pid;
    int _quantity;
    Region _region;
    
public:
    ProductInventory (int pid_, int quantity_, Region region_) :
    _pid (pid_),
    _quantity (quantity_),
    _region (region_) {};
    
    ProductInventory (const ProductInventory &other_) {
        _pid = other_._pid;
        _quantity = other_._quantity;
        _region = other_._region;
    }
    
    const int getPid () const { return _pid; }
    const int getQuantity () const { return _quantity; }
    void reduceQuantity (int val) { _quantity -= val; }
    const Region getRegion () const { return _region; }
};

#endif /* ProductInventory_hpp */
