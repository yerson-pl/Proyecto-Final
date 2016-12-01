app
//------------------------------
// TODO: API menu
// por lo pronto colocar aqui el menu para su Modelo, vease test1
//------------------------------
    .factory("menuService", function(authService) {

    var sections = [
        /*
        {
          title: 'Getting Started',
          state: 'getting-started',
          url: '/getting-started',
          type: 'link'
        }
        */
    ];

    /*sections.push({
        title: 'Dashboard',
        state: 'app.dashboard',
        type: 'link'
    });*/
    /**
        sections.push({
            //title: 'Sección ui',
            //type: 'heading',
            menu: [{
                title: 'U.I.',
                state: 'ui',
                type: 'toggle',
                menu_items: [{
                    title: 'Test 1 uno más',
                    state: 'ui.test1',
                    type: 'link'
                }, {
                    title: '2Test 2',
                    state: 'ui.test2',
                    type: 'link'
                }, {
                    title: 'Test 3',
                    state: 'ui.test3',
                    type: 'link'
                }, {
                    title: 'Test 4',
                    state: 'ui.test4',
                    type: 'link'
                }, {
                    title: 'Test 5',
                    state: 'ui.test5',
                    type: 'link'
                }, {
                    title: 'Test Directivas',
                    state: 'ui.dir',
                    type: 'link'
                }, ]
            }]
        });
    **/
    sections.push({

        menu: [{
            title: 'Sistema',
            type: 'toggle',
            state: 'auths.system',
            menu_items: [
                /**
                {
                    title: 'xx',
                    state: 'auths.system.xx',
                    type: 'link'
                }, {
                    title: 'Grupos',
                    state: 'auths.system.ct',
                    type: 'link'
                }, **/
                {
                    title: 'Permisos',
                    state: 'auths.system.permission',
                    type: 'link'
                }, {
                    title: 'Menu',
                    state: 'auths.system.menu',
                    type: 'link'
                }, {
                    title: 'Log',
                    state: 'auths.system.log',
                    type: 'link'
                },
            ]
        }]
    });


    sections.push({
        menu: [{
            title: 'Catálogo',
            type: 'toggle',
            state: 'catalogo.catalogo',
            menu_items: [{
                title: 'Categorías',
                state: 'catalogo.catalogo.categorias',
                type: 'link'
            }, {
                title: 'Autores',
                state: 'catalogo.catalogo.autores',
                type: 'link'
            }, ]
        }]
    });

    sections.push({
        menu: [{
            title: 'Asociación',
            type: 'toggle',
            state: 'asociacion.asociacion',
            menu_items: [{
                title: 'Asociacion',
                state: 'asociacion.asociacion.asociacion',
                type: 'link'
            }, {
                title: 'Cuenta bancaria',
                state: 'asociacion.asociacion.banco',
                type: 'link'
            }, ]
        }]
    });

    sections.push({

        menu: [{
            title: 'Eventos',
            type: 'toggle',
            state: 'eventos.eventos',
            menu_items: [{
                title: 'Eventos',
                state: 'eventos.eventos.eventos',
                type: 'link'
            }, {
                title: 'Asistencias',
                state: 'eventos.eventos.asistencias',
                type: 'link'
            }, ]
        }]
    });


    authService.getMenu().then(function(r) {
        menu = r.data;
        console.log("menuService.authService.getMenu():" + JSON.stringify(menu));
        sections.push(
            menu
        );

    }, function(error) {
        console.log("error in menuService.authService.getMenu():" + JSON.stringify(error));
    });

    return {
        sections: sections,
    };
});
