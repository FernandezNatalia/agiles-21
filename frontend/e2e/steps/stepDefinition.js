var {Given, When, Then, Before} = require('cucumber');    
const { browser, element } = require('protractor');  
  
  
Before({timeout: 60 * 1000}, function() {  
  // Does some slow browser/filesystem/network actions  
  browser.manage().window().maximize();  
});  
  
Given(/^open the application "([^"]*)"$/, function (string) {  
    return  browser.get(string);  
});  
  
When('user login with {string} and {string}', function (string, string2) {  
  // Write code here that turns the phrase above into concrete actions  
  element(by.model('Auth.user.name')).sendKeys(string);  
  element(by.model('Auth.user.password')).sendKeys(string2);  
  return console.log("entered the user name and password");  
});  
  
When('User enters the Admin {string}', function (string) {  
  // Write code here that turns the phrase above into concrete actions  
  element(by.model('model[options.key]')).sendKeys(string);  
  return console.log("enetered the logged in user name");  
    
});  
Then('user should login succcessfully', function () {  
  // Write code here that turns the phrase above into concrete actions  
  return console.log("success");  
}); 