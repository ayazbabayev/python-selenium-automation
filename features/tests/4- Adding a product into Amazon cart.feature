# Created by Ayaz
Feature: Adding a product into Amazon cart

  Scenario: User can add a product into Amazon cart
    Given User opens Amazon page (No Sign In)
    When User searches for Al Mokha: The World's First Coffee. Yemen Medium Roast (whole bean)
    And User selects the product
    And User adds product into cart
    And User clicks Amazon cart icon
    Then Cart shows Al Mokha: The World's First Coffee. Yemen Medium Roast (whole bean) in the cart
