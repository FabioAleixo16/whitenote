google.charts.load('current', {packages: ['corechart']});
google.charts.setOnLoadCallback(drawChart);
            
            function drawChart() {
      
                // Clientes
                var dataclientes = google.visualization.arrayToDataTable([
                    ['Element', 'Density', { role: 'style' }],
                    ['Ativos', 23, 'green'],
                    ['Não compram à mais de 90 dias', 12, 'red']
                 ]);

                 var optionsclientes = {
                    title: "Estado dos clientes",
                    width: 600,
                    height: 400,
                    bar: {groupWidth: "95%"},
                    legend: { position: "none" },
                  };

                 var chartclientes = new google.visualization.ColumnChart(document.getElementById("graficoclientes"));
                 chartclientes.draw(dataclientes, optionsclientes);


                 // Fornecedores
                var datafornecedores = google.visualization.arrayToDataTable([
                    ['Element', 'Density', { role: 'style' }],
                    ['Gold', 23, 'gold'],
                    ['Silver', 12, 'silver']
                 ]);

                 var optionsfornecedores = {
                    title: "Estado dos fornecedores",
                    width: 600,
                    height: 400,
                    bar: {groupWidth: "95%"},
                    legend: { position: "none" },
                  };

                 var chartfornecedores = new google.visualization.ColumnChart(document.getElementById("graficofornecedores"));
                 chartfornecedores.draw(datafornecedores, optionsfornecedores);

                 // Produtos
                var dataprodutos = google.visualization.arrayToDataTable([
                    ['Element', 'Density', { role: 'style' }],
                    ['+ vendidos', 23, 'gold'],
                    ['- vendidos', 12, 'silver']
                 ]);

                 var optionsprodutos = {
                    title: "Estado dos produtos",
                    width: 600,
                    height: 400,
                    bar: {groupWidth: "95%"},
                    legend: { position: "none" },
                  };

                 var chartprodutos = new google.visualization.ColumnChart(document.getElementById("graficoprodutos"));
                 chartprodutos.draw(dataprodutos, optionsprodutos);

                 // Utilizadores
                var datautilizadores = google.visualization.arrayToDataTable([
                    ['Element', 'Density', { role: 'style' }],
                    ['Ativos', 23, 'green'],
                    ['Inativos', 12, 'yellow'],
                    ['Bloqueados', 3, 'red'],
                 ]);

                 var optionsutilizadores = {
                    title: "Estado dos utilizadores",
                    width: 600,
                    height: 400,
                    bar: {groupWidth: "95%"},
                    legend: { position: "none" },
                  };

                 var chartutilizadores = new google.visualization.ColumnChart(document.getElementById("graficoutilizadores"));
                 chartutilizadores.draw(datautilizadores, optionsutilizadores);
            }