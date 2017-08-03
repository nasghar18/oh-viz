Outcome Health DataTables Integration
=====================================

DataTables is a framework designed to make displaying data more organized and intuitive. 

The goal of the DataTable integration is to use that framework and plug in IAT and other data so as to have access to and make using that data easier.

The way it's been integrated with OH's data is as follows:

First, DataTables, JQuery, and Bootstrap are linked to using their respective CDNs.

Then there must be a <table> within the HTML with an id that will be used to call on later so DataTables has somewhere to plug in all of the rendered data. In this case the id is *example*:

.. code-block:: html

	<div id="example_wrapper" class="dataTables_wrapper form-inline dt-bootstrap no-footer">
  
      <table id="example" class="table table-striped table-bordered dataTable no-footer" cellspacing="0" width="100%" role="grid" aria-describedby="example_info" style="width: 100%;">
       
      </table>
    </div>


Using Python, the data is first converted into a variable DataTables can use:

.. code-block:: python

	def index():

	df = pd.read_csv('static/data/2ndiat.csv')[['analyst','create_dt','iat_id','iat_name','summary_offices']]
	csv = df.to_json(orient='records')

	secdf = pd.read_csv('static/data/iat.csv')[['analyst','create_dt','iat_id','iat_name','summary_offices']]
	seccsv = secdf.to_json(orient='records')

	return render_template("test.html",test=test,csv=csv, seccsv=seccsv)

In Javascript:

.. code-block:: javascript

	   	var dataSet = {{csv|safe}};
		var secdataSet = {{seccsv|safe}};

The data is now stored in the variables *dataSet* and *secdataSet*

Before DataTables, a function is made to allow DataTables to render one of the data columns as links, the links themselves to be added at a later point: 

.. code-block:: javascript

		function LINKFunc(data, type, row, meta){
                    if(type === 'display'){
                      return '<a href="'+ row["summary_offices"]+'">'+data+'</a>';
                    } else {
                      console.log("missing");
                      return 0
                    };
                  };

Once the function is created, JQuery is used to call on DataTables' functions and dynamically create a table:

.. code-block:: javascript

	$(document).ready(function(){
        $('#example').DataTable( {
            "data": dataSet,
            "columns": [
                { "data": "iat_id",
                  "render": LINKFunc,
                  "title": "IAT ID"
                },
                {"data": "iat_name", title: "IAT NAME"},
                {"data": "analyst", title: "ANALYST"},
                {"data": "create_dt", title: "CREATED"},
                {"data": "summary_offices", title: "Summary Offices"}
            ],
            
            "lengthChange": false,
            "pageLength": 27,
            "dom": "<'row'<'col-sm-6'l><'col-sm-6'f>>" + "<'row'<'col-sm-12'tr>>" + "<'row'<'col-sm-5'i><'col-sm-7'p>>"
	} );
	});

In the above code first there is "data" which receives where the data is coming from, in this case the variable *dataSet*. 

Next, columns are rendered dynamically in the "columns" section. Within the section each piece of "data" shows which set of data should be plugged in (for example the first column is *iat_id*, second is *iat_name*, etc.), how it should be rendered (optional), and what that specific column title should be.

"render" was only used in the first column because the *LINKFunc* function is beng used to create links for every piece of data in that column, and so it's being rendered differently than DataTables' default setting. Every other column is being rendered in DataTables' natural setting.

DataTables has many built-in features that allow for the customization of how engaging the table can be. THe features added here are "lengthChange", "pageLength", and "dom".

"lengthChange" allows Users to change how much data is being displayed on the page. It is controlled through a boolean and in this case has been turned off with *false*.

In turning off that feature, a default amount of data to be displayed can be set. "pageLength" allows for that to be set, currently set to 27.

Lastly "dom" allows for each feature of the table to be custom sized. The different letters following each piece of html refer to a different feature. The legend for all the features can be found within the DataTables documentation.

DataTables can be manipulated to have multiple tables on a page with different sizes and features, all coming from different data sources.

More information on how to further use DataTables can be found on the DataTables website.





	