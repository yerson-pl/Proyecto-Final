app
    .provider('router', function($stateProvider) {
        var urlCollection;
        this.$get = function($http, $state) {
            return {
                setUpRoutes: function() {
                    $http.get(urlCollection).success(function(collection) {
                        // solo para subibr el json al localStorage
                        localStorage.setItem('collection', JSON.stringify(collection));
                        /*for (var routeName in collection) { // activar el for para generar router dinámicos aquí
                            if (!$state.get(routeName)) {
                                $stateProvider.state(routeName, collection[routeName]);
                            }
                        }*/
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
        router.setUpRoutes(); // activar para generar router dinámicos aquí
    })
    //==================================
    // base routers
    //==================================
    .config(function($stateProvider, $urlRouterProvider, routerProvider) {

        routerProvider.setCollectionUrl('http://localhost:9000/api/auths/routers/');

        $stateProvider
            .state('access', {
                //==================================
                // access page
                //==================================
                url: '/access',
                template: '<div class="indigo bg-big"><div ui-view class="fade-in-down smooth"></div></div>'
            })
            .state('access.signin', {
                //==================================
                // signin page
                //==================================

                url: '/signin',
                controller: "loginController",
                templateUrl: 'auth_web_apps/access_web/views/pages/login.html'
            })
            .state('access.signup', {
                //==================================
                // signup page
                //==================================

                url: '/signup',
                templateUrl: 'auth_web_apps/access_web/views/pages/signup.html'
            })
            .state('access.forgot-password', {
                //==================================
                // forgot-password page
                //==================================
                url: '/forgot-password',
                templateUrl: 'auth_web_apps/access_web/views/pages/forgot-password.html'
            })
            .state('access.lockme', {
                //==================================
                // lockme page
                //==================================
                url: '/lockme',
                templateUrl: 'auth_web_apps/access_web/views/pages/lockme.html'
            });
    });
