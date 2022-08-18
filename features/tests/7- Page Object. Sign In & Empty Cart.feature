# Created by ababa at 8/16/2022
Feature: AMAZON HEADER PART FUNCTIONALITY

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
     When Click Amazon Orders link
     Then Verify Sign In page is opened

    Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify "Your Shopping Cart is empty." text present

    Scenario: User can add a product into Amazon cart
    Given Open Amazon page
    When User will search for tea
    And User will select the product
    And User will add product into cart
    And Click on cart icon
    Then Verify 1 item is shown in the cart