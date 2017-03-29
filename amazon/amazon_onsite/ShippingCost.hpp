//
//  ShippingCost.hpp
//  Amazon
//
//  Created by Hawsang on 11/30/16.
//  Copyright © 2016 LeightonSt. All rights reserved.
//

#ifndef ShippingCost_hpp
#define ShippingCost_hpp

#include "misc.h"

class ShippingCost {
private:
    Region _ship_from;
    Region _ship_to;
    Method _method;
    int _cost_per_item;
    int _days;
    
public:
    ShippingCost (Region ship_from_, Region ship_to_, Method method_, int cost_per_item_, int days_) :
    _ship_from (ship_from_),
    _ship_to (ship_to_),
    _method (method_),
    _cost_per_item (cost_per_item_),
    _days (days_) {};
    
    ShippingCost (const ShippingCost &_other) {
        _ship_from = _other._ship_from;
        _ship_to = _other._ship_to;
        _method = _other._method;
        _cost_per_item = _other._cost_per_item;
        _days = _other._days;
    }
    
    const Region getShipFrom () const { return _ship_from; }
    const Region getShipTo () const { return _ship_to; }
    const int getDays () const { return _days; }
    const int getCost () const { return _cost_per_item; }
};

#endif /* ShippingCost_hpp */
