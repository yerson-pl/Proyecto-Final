app

//==================================
// app main routers
//==================================
    .config(function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise("/access/signin");

    $stateProvider
        .state("notauthorized", {
            //==================================
            // Not Authorized page
            //==================================
            url: "/notauthorized",
            templateUrl: "app/views/pages/notauthorized.html"
        })

    .state("apps", {
        //==================================
        // Apps page (Main)
        //==================================
        url: "/apps",
        data: { page: 'Apps page' },
        views: {
            '': {
                templateUrl: "app/views/pages/apps.tmpl.html"
            },
        }
    })

    .state('404', {
        //==================================
        // 404 page
        //==================================
        url: '/404',
        templateUrl: 'app/views/pages/404.html'
    })

    .state('505', {
        //==================================
        // 505 page
        //==================================
        url: '/505',
        templateUrl: 'app/views/pages/505.html'
    });

});
