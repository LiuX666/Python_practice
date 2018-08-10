

/*******************************************************************************
 * 请求Ajax 带返回值（JSON）； url： 表示请求路径 、 parm： 条件参数 、 callback： 回调方法
 * --------------------------------------------------
 */
function getAjaxJson(url, param, callBack, method, contentType, async) {
	if (contentType == null || contentType == undefined) {
		contentType = "application/x-www-form-urlencoded";
	}
	if (async == null || async == undefined) {
		async = true;
	}
	if (method == null || method == undefined) {
		method = "GET";
	}
	$.ajax({
		url : url,
		type : method,
		datatype : "json",
		contentType : contentType,
		data : param,
		async : async,
		success : function(res) {
			callBack(res);
		},
		error : HandleAjaxException,
	// 超时
	});
}


/*******************************************************************************
 * 处理Ajax请求超时 ;request：XMLHttpRequest、status：状态
 * --------------------------------------------------
 */
function HandleAjaxException(XMLHttpRequest, status) {
	if (status == 'error') {// 超时
		alert("请求异常");
		return;
	}
}

// 格式化时间
Date.prototype.format = function(format) {
	var o = {
		"M+" : this.getMonth() + 1,
		"d+" : this.getDate(),
		"h+" : this.getHours(),
		"m+" : this.getMinutes(),
		"s+" : this.getSeconds(),
		"q+" : Math.floor((this.getMonth() + 3) / 3),
		"S" : this.getMilliseconds()
	}
	if (/(y+)/.test(format)) {
		format = format.replace(RegExp.$1, (this.getFullYear() + "")
				.substr(4 - RegExp.$1.length));
	}
	for ( var k in o) {
		if (new RegExp("(" + k + ")").test(format)) {
			format = format.replace(RegExp.$1, RegExp.$1.length == 1 ? o[k]
					: ("00" + o[k]).substr(("" + o[k]).length));
		}
	}
	return format;
}


// 警告提示框
function showModalWarnMsg(message, callback) {
	$("#warn-modal .modal-body span").html(message);
	$("#warn-modal").modal("show");
	$(".dialog-warn-button").unbind("click");
	$(".dialog-warn-button").click(function() {
		if (callback != undefined) {
			callback();
		}
		$("#warn-modal").modal("hide");
	});
	$('#warn-modal').on('hide.bs.modal', function() {
		$("#warn-modal .modal-footer span.error").html("");
	})
}


// 校验
function validateDataType(data, type) {
	return (typeof data) == type;
}

function removeValidation() {
	var list = $(".error");
	for (var i = 0; i < list.length; i++) {
		$(list[i]).html("");
	}
}