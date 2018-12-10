itemDict = {
            # Basic : Gatherers #
            'Coal'              : 0,
            'Copper'            : 1,
            'Fish'              : 2,
            'Gas'               : 3,
            'Iron'              : 4,
            'Oil'               : 5,
            'Sand'              : 6,
            'Water'             : 7,
            'Wood'              : 8,
            # Basic : Farms #
            'Hops'              : 9,
            'Potato'            : 10,
            'Vegetables'        : 11,
            'Wheat'             : 12,
            'Apples'            : 13,
            'Grapes'            : 14,
            'Olives'            : 15,
            'Oranges'           : 16,
            'Raw Rubber'        : 17,
            'Berries'           : 18,
            'Cocoa'             : 19,
            'Cotton'            : 20,
            'Sugar'             : 21,
            'Beef'              : 22,
            'Chicken'           : 23,
            'Eggs'              : 24,
            'Leather'           : 25,
            'Milk'              : 26,
            'Mutton'            : 27,
            'Wool'              : 28,
            # Rural : Food Factory #
            'Beef Stew'         : 29,
            'Berry Pie'         : 30,
            'Burgers'           : 31,
            'Cheese'            : 32,
            'Chicken Dinner'    : 33,
            'Chocolate Bar'     : 34,
            'Chocolate Cake'    : 35,
            'Cooked Vegetables' : 36,
            'Dough'             : 37,
            'Flour'             : 38,
            'Fried Chicken'     : 39,
            'Olive Oil'         : 40,
            'Pizza'             : 41,
            'Waffles'           : 42,
            # Rural : Preservation Factory #
            'Bag of Chips'      : 43,
            'Canned Fish'       : 44,
            'Canned Mutton'     : 45,
            'Chicken Soup'      : 46,
            'Soup'              : 47,
            # Rural : Dinks Factory
            'Apple Smoothie'    : 48,
            'Berry Smoothie'    : 49,
            'Grape Juice'       : 50,
            'Orange Juice'      : 51,
            'Orange Soda'       : 52,
            'Soda Water'        : 53,
            }


# ID - Output - Input - Type
buildingDict = {
                # Basic : Gatherers
                'Coal Mine'             : [0, 
                                           [['Coal', 10, 1]],
                                           [[]],
                                           "Gatherer"
                                          ],
                'Copper Mine'           : [1, 
                                           [['Copper', 10, 1]],
                                           [[]],
                                           "Gatherer"
                                          ],
                'Fisherman Pier'        : [2, 
                                           [['Fish', 10, 1]],
                                           [[]],
                                           "Gatherer"
                                          ],
                'Gas Pump'              : [3, 
                                           [['Gas', 10, 1]],
                                           [[]],
                                           "Gatherer"
                                          ],
                'Iron Mine'             : [4, 
                                           [['Iron', 10, 1]],
                                           [[]],
                                           "Gatherer"
                                          ],
                'Lumberyard'            : [5, 
                                           [['Wood', 10, 1]],
                                           [[]],
                                           "Gatherer"
                                          ],
                'Offshore Oil Drill'    : [6, 
                                           [['Oil', 10, 1]],
                                           [[]],
                                           "Gatherer"
                                          ],
                'Oil Drill'             : [7, 
                                           [['Oil', 10, 1]],
                                           [[]],
                                           "Gatherer"
                                          ],
                'Sand Collector'        : [8, 
                                           [['Sand', 10, 1]],
                                           [[]],
                                           "Gatherer"
                                          ],
                'Water Siphon'          : [9, 
                                           [['Water', 10, 1]],
                                           [[]],
                                           "Gatherer"
                                          ],
                # Basic : Farms
                'Crop Farm Hops'        : [10, 
                                           [['Hops', 45, 2]],
                                           [['Water', 45, 1]],
                                           "Farm"
                                          ],
                'Crop Farm Potato'      : [11, 
                                           [['Potato', 45, 2]],
                                           [['Water', 45, 1]],
                                           "Farm"
                                          ],
                'Crop Farm Vegetables'  : [12, 
                                           [['Vegetables', 45, 2]],
                                           [['Water', 45, 1]],
                                           "Farm"
                                          ],
                'Crop Farm Wheat'       : [13, 
                                           [['Wheat', 45, 2]],
                                           [['Water', 45, 1]],
                                           "Farm"
                                          ],
                'Livestock Farm Cow'    : [14, 
                                           [['Beef', 45, 1], ['Milk', 45, 1], ['Leather', 45, 1]],
                                           [['Water', 45, 1], ['Wheat', 45, 2]],
                                           "Farm"
                                          ],
                'Livestock Farm Chicken': [15, 
                                           [['Chicken', 30, 1], ['Eggs', 30, 2]],
                                           [['Water', 30, 1], ['Wheat', 30, 1]],
                                           "Farm"
                                          ],
                'Livestock Farm Sheep'  : [16, 
                                           [['Mutton', 30, 1], ['Wool', 30, 2]],
                                           [['Water', 30, 1], ['Wheat', 30, 1]],
                                           "Farm"
                                          ],
                'Orchard Apples'        : [17, 
                                           [['Apples', 35, 2]],
                                           [['Water', 35, 1]],
                                           "Farm"
                                          ],
                'Orchard Grapes'        : [18, 
                                           [['Grapes', 35, 2]],
                                           [['Water', 35, 1]],
                                           "Farm"
                                          ],
                'Orchard Olives'        : [19, 
                                           [['Olives', 35, 2]],
                                           [['Water', 35, 1]],
                                           "Farm"
                                          ],
                'Orchard Oranges'       : [20, 
                                           [['Oranges', 35, 2]],
                                           [['Water', 35, 1]],
                                           "Farm"
                                          ],
                'Orchard Rubber'        : [21, 
                                           [['Raw Rubber', 35, 2]],
                                           [['Water', 35, 1]],
                                           "Farm"
                                          ],
                'Plantation Berries'    : [22, 
                                           [['Berries', 30, 2]],
                                           [['Water', 30, 1]],
                                           "Farm"
                                          ],
                'Plantation Cocoa'      : [23, 
                                           [['Cocoa', 30, 2]],
                                           [['Water', 30, 1]],
                                           "Farm"
                                          ],
                'Plantation Cotton'     : [24, 
                                           [['Cotton', 30, 2]],
                                           [['Water', 30, 1]],
                                           "Farm"
                                          ],
                'Plantation Sugar'      : [25, 
                                           [['Sugar', 30, 2]],
                                           [['Water', 30, 1]],
                                           "Farm"
                                          ],
                # # Factory: Rural
                # 'Food Factory'          : 14,
                # 'Preservation Factory'  : 15,
                # 'Drinks Factory'        : 16,
                }
