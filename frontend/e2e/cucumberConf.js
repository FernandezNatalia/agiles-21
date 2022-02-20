exports.config = {  
    //seleniumAddress: 'http://127.0.0.1:4444/wd/hub',  
    directConnect:true,  
    getPageTimeout: 60000,  
    allScriptsTimeout: 500000,  
    framework: 'custom',  
    frameworkPath: require.resolve('protractor-cucumber-framework'),  
    capabilities: {  
      'browserName': 'chrome'  
    },  
    specs: [  
      'features/*.feature'  
    ],    
    cucumberOpts: {  
      require: 'steps/*.js',  
      tags: false,  
      
    },
    onPrepare: function () {
        browser.manage().window().maximize();
    }
}; 