var targetIp="http://127.0.0.1:5000";
var flag=0;

function getDataUrl(url,obj){
	getAjaxJson(url, null, function(res) {
		var tmp = [];
		for(var prop in res){
          tmp.push({
                id:res[prop][0],
                name:res[prop][1],
                age:res[prop][2],
          })
		}
		obj.listdata = tmp;
	}, "GET","application/JSON");

};

var SdataList = new Vue(
			{
				data : {listdata:[]},	
				created:function(){
					getDataUrl(targetIp+"/get",this);			
				},
				updated : function() {
                    this.$nextTick(function(){
						$(".remove").click(function() {
							var Sid = $(this).parents("tr").attr("s-id");
							showModalWarnMsg("是否移除该条记录",function() {
                              getAjaxJson(targetIp+"/delete/"+Sid, null, function(res) {
	  	     
                              getDataUrl(targetIp+"/get",SdataList);	
		             
	                          }, "GET","application/JSON"); 
	                        })               
				       })
                       
                       $(".update").click(function() {   
                             flag=0;                   	
							var Sid = $(this).parents("tr").attr("s-id");
                            getAjaxJson(targetIp+"/getone/"+Sid, null, function(res) {
                            	  $("#Tid").val(res[0]);
                                  $("#id").val(res[0]);
                            	  $("#sname").val(res[1]);
                            	  $("#age").val(res[2]);
                            	  $(".modalT").html("更新窗口");
		                          $("#addData").modal("show");
	                        }, "GET","application/JSON");                
				       })

					})
				},	
				
			});	


function loadList(){
	SdataList.$mount(".datalist");
}


function addsdata(){
	$(".stu-add").click(function() {
		 flag=1;
		$(".modalT").html("新增窗口");
		$("#addData").modal("show");
	});
}

 
function dataSub(){
	var dataS=""
	var listS = $(".data-body .form-group");

	for (var i = 0; i < listS.length; i++) {
		var keyS = $(listS[i]).children("label").attr("index").replace(
				/(^\s*)|(\s*$)/g, "");
		var valueS = $(listS[i]).children("input").val().replace(
				/(^\s*)|(\s*$)/g, "");
		dataS += "\"" + keyS + "\":\"" + valueS + "\""
		if (i < listS.length - 1) {
			dataS += ",";
		}
	}

	paramS = "{" + dataS + "}";
}


function dataSubmit(){
	  $(".data-submit").click(function() {
	  if (!validator.form()) {
			    return;
		  }
	  dataSub();
	  if(flag==1){
        getAjaxJson(targetIp+"/insert", paramS, function(res) {
	  	$("#addData").modal("hide");
		$("#addData").on("hidden.bs.modal",function() {
              getDataUrl(targetIp+"/get",SdataList);	
		})
	    }, "POST","application/JSON");
	  }else if(flag==0){
         var uid= $("#Tid").val();
	     getAjaxJson(targetIp+"/update/"+uid, paramS, function(res) {
	  	 $("#addData").modal("hide");
		 $("#addData").on("hidden.bs.modal",function() {
              getDataUrl(targetIp+"/get",SdataList);
              flag=0;	
		 })
	    }, "POST","application/JSON");
	  }

	});
	
}


var validator = null;
function dataValidation() {
	    validator = $("#edit-form").validate({
		focusCleanup:true,
	    onfocusout: function(element) { $(element).valid(); },  
		rules : {
	         "id": {
				required : true,
				min:1,
				max:999999999
			},
			"sname": {
				required : true,
				
			},
			"age": {
				required : true,
				min:1,
				max:100
			},
		},
		messages : {
			"id": {
				required : "不能为空",
				min:"输入的值不能小于 1",
				max:"输入的值不能大于999999999"
			},
			"sname": {
				required : "不能为空",
			},
			"age": {
				required : "不能为空",
				min:"输入的值不能小于 1",
				max:"输入的值不能大于100"
			},
		},
		errorPlacement : function(error, element) {
			var html = error.html();
			error.appendTo(element.parent());
			
		},
		
	});

	validator.form();
}

function modalhidden(){
	$("#addData").on("hidden.bs.modal", function() {
		removeValidation();
		$("#edit-form")[0].reset();
	});
}


$(function(){
	loadList();
	addsdata();
	dataSubmit();
	dataValidation();
	modalhidden();
})

