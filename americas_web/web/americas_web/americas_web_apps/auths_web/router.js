app
//==================================
// auths routers
//==================================
    .config(function($stateProvider, $urlRouterProvider) {

    $stateProvider
        .state('auths', {
            //==================================
            // auths layout base
            //==================================
            url: '/auths',
            views: {
                '': {
                    templateUrl: 'app/views/layout.html'
                },
                'aside': {
                    templateUrl: 'app/views/aside.html'
                },
                'content': {
                    templateUrl: 'app/views/content.html'
                }
            }
        })
        .state('auths.system', {
            //==================================
            // auths system page
            //==================================
            url: '/system',
            template: '<div ui-view ></div>'
        })
        .state("auths.system.ct", {
            //==================================
            // url ct
            //==================================
            url: "/ct",
            data: { section: 'System', page: 'Document' },
            templateUrl: "app/views/pages/document.html"
        })
        .state('auths.hierarchy', {
            //==================================
            // url hierarchy
            //==================================
            url: '/hierarchy',
            template: '<div ui-view ></div>'
        })
        .state("auths.hierarchy.hierarchy_type", {
            url: "/hierarchy_type",
            data: { section: 'Hierarchys', page: 'Hierarchy Type' },
            templateUrl: "americas_web_apps/auths_web/views/hierarchy_type/index.html"
        })
        .state("auths.system.permission", {
            url: "/permission",
            data: { section: 'System', page: 'Permisos' },
            templateUrl: "americas_web_apps/auths_web/views/permission/index.html"
        })
        .state("auths.system.contenttype", {
            url: "/contenttype",
            data: { section: 'System', page: 'Aplicaciones' },
            templateUrl: "americas_web_apps/auths_web/views/contenttype/index.html"
        })
        .state("auths.system.log", {
            url: "/log",
            data: { section: 'System', page: 'Logs' },
            templateUrl: "americas_web_apps/auths_web/views/log/index.html"
        })
        .state("auths.system.menu", {
            //==================================
            // url Menú
            //=================================
            url: "/menu",
            data: { section: 'System', page: 'Menú' },
            templateUrl: "americas_web_apps/auths_web/views/menu/index.html",

            settings: {
                //loginRequired: true,
                //roles: ['User'],
            },
            resolve: {
                //checkSecurity: checkSecurity,
            },
        });

});
