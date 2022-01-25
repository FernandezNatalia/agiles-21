Feature: Login    
    In order to login to the application    
    As a User    
    I need to enter the Valid username and Password    
    
    Scenario: In order to login to the angular app    
        Given open the application "http://www.way2automation.com/angularjs-protractor/registeration/#/login"   
        When user login with "angular" and "password"  
        And User enters the Admin "TestUser"  
        Then user should login succcessfully  