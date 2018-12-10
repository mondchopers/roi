## Example Script of game situation calculation ##

import itemkey as itk
from library import cBuilding, cCompany

assets = [cBuilding('Water 1', 'Water Siphon', 3, 0.333),
          cBuilding('Wheat 1', 'Crop Farm Wheat', 3, 0.75),
          ]
company = cCompany(assets)
company.print_net_production()