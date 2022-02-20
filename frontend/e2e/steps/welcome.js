var {Given, When, Then, Before} = require('cucumber');    
const { browser, element } = require('protractor');  
  
Before({timeout: 60 * 1000}, function() {  
  // Does some slow browser/filesystem/network actions  
  browser.manage().window().maximize();  
});  

Given('user enter into the game succcessfully', function () {      
  // Write code here that turns the phrase above into concrete actions
  return 'pending';
  });
  

Then('user must see the drawing of Hangman', function () {
  // Write code here that turns the phrase above into concrete actions       
  return 'pending';
});

Then('user must see the keyboard', function () {
  // Write code here that turns the phrase above into concrete actions       
  return 'pending';
});

Then('user must see a navbar', function () {
  // Write code here that turns the phrase above into concrete actions       
  return 'pending';
});