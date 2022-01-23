import { Given, When, Then } from '@cucumber/cucumber';

Given("today is Sunday", function() {
    console.log("Step parsed.");
});

When("I ask whether it's Friday yet", function() {
    console.log("Step parsed.");
});

Then("I should be told {string}", function(variable) {
    console.log(variable);
});