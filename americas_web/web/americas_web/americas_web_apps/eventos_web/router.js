app
    .provider('router', function($stateProvider) {
        var urlCollection;
        this.$get = function($http, $state) {
            return {
                setUpRoutes: function() {
                    $http.get(urlCollection).success(function(collection) {
                        //console.log('collection::' + JSON.stringify(collection));
                        for (var routeName in collection) {
                            if (!$state.get(routeName)) {
                                $stateProvider.state(routeName, collection[routeName]);
                            }
                        }
                    });
                }
            };
        };
        this.setCollectionUrl = function(url) {
            urlCollection = url;
        };
    });

app
    .run(function(router) {
        // no recupera el foco porque el run se genera después del config
        //router.setUpRoutes();
    })
    .config(function($stateProvider, $urlRouterProvider, ROUTERS3, routerProvider) {
        collection = ROUTERS3;
        for (var routeName in collection) {
            //if (!$state.get(routeName)) {
            $stateProvider.state(routeName, collection[routeName]); // $stateProvider.state debe generarse aqui para no perder el foco
            //}
        }

        //routerProvider.setCollectionUrl('routeCollection.json');
    })

;
