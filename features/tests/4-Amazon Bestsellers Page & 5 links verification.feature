# Created by ababa at 7/22/2022
Feature: Amazon Bestsellers page - 5 links verification


  Scenario: User can navigate to Bestsellers page and see 5 links
    Given User opens Amazon page (No Sign In)
    When User clicks on Bestsellers page
    Then Verify that 5 links are present

