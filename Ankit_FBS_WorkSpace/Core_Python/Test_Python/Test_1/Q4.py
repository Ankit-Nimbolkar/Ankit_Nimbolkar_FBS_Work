# 4. Calculate the cost of painting the following building's walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and
# exterior wall.
# Note: 1. Below diagram is of two joint rooms
#         2. It is upper view of building.


Area_wall = float(input("Enter Area of One Wall in square feet : "))
Interior_cost = int(input("Enter Cost of interior wall painting per 1sq feet : "))
Exterior_cost = int(input("Enter Cost of Exterior wall painting per 1sq feet : "))
Total_interior_walls = 8
Total_Exterior_walls = 7

Costofallwallinterior = (Area_wall * Interior_cost) *  Total_interior_walls
CostofallwallExterior = (Area_wall * Exterior_cost ) * Total_Exterior_walls
TotalCostOfPaint = Costofallwallinterior + CostofallwallExterior

print(f'Total Interior walls --> {Total_interior_walls}')
print(f'Total Exterior walls --> {Total_Exterior_walls}')
print(f'Total Cost for painting interior of all wall is {Costofallwallinterior}')
print(f'Total Cost for painting Exterior of all wall is {CostofallwallExterior}')
print(f'Total Cost for painting Exterior + interior of all wall is {TotalCostOfPaint}')