Outcome Health DataTables Integration
=====================================

DataTables is a framework designed to make displaying data more organized and intuitive. 

The goal of the DataTable integration is to use that framework and plug in IAT and other data so as to have access to and make using that data easier.

The way it's been integrated with OH's data is as follows:

The data is first converted into a variable DataTables can use:

.. code-block::Python

def index():

df = pd.read_csv('static/data/2ndiat.csv')[['analyst','create_dt','iat_id','iat_name','summary_offices']]
csv = df.to_json(orient='records')

secdf = pd.read_csv('static/data/iat.csv')[['analyst','create_dt','iat_id','iat_name','summary_offices']]
seccsv = secdf.to_json(orient='records')

return render_template("test.html",test=test,csv=csv, seccsv=seccsv)

And in Javascript:

	   	::

	   	var dataSet = {{csv|safe}};
		var secdataSet = {{seccsv|safe}};

The data is now stored in the variables *dataSet* and *secdataSet*

Before DataTables, a function is made to allow DataTables to render one of the data columns as links, the links themselves to be added at a later point: 

		::

		function LINKFunc(data, type, row, meta){
                    if(type === 'display'){
                      return '<a href="'+ row["summary_offices"]+'">'+data+'</a>';
                    } else {
                      console.log("missing");
                      return 0
                    };
                  }; 



	