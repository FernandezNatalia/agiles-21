exports.config = {  
    //seleniumAddress: 'http://127.0.0.1:4444/wd/hub',  
    directConnect:true,  
    getPageTimeout: 60000,  
    allScriptsTimeout: 500000,  
    framework: 'custom',  
    // path relative to the current config file  
    frameworkPath: require.resolve('protractor-cucumber-framework'),  
    capabilities: {  
      'browserName': 'chrome'  
    },  
      
    // Spec patterns are relative to this directory.  
    specs: [  
      'features/*.feature'  
    ],  
  
    cucumberOpts: {  
      require: 'steps/stepDefinition.js',  
      tags: false,  
      
    },
    onPrepare: function () {
        browser.manage().window().maximize(); // maximize the browser before executing the feature files
    }
}; 