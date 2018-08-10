/**
 * Bootstrap文字本地化
 */
(function($) {
	'use strict';
	$.fn.bootstrapTable.locales['zh-CN'] = {
		formatLoadingMessage : function() {
			return '正在努力地加载数据中，请稍候……';
		},
		formatRecordsPerPage : function(pageNumber) {
			return '每页显示 ' + pageNumber + ' 条记录';
		},
		formatShowingRows : function(pageFrom, pageTo, totalRows) {
			return '显示第 ' + pageFrom + ' 到第 ' + pageTo + ' 条记录，总共 ' + totalRows
					+ ' 条记录';
		},
		formatSearch : function() {
			return '搜索';
		},
		formatNoMatches : function() {
			return '没有找到匹配的记录';
		},
		formatPaginationSwitch : function() {
			return '隐藏/显示分页';
		},
		formatRefresh : function() {
			return '刷新';
		},
		formatToggle : function() {
			return '切换';
		},
		formatColumns : function() {
			return '列';
		},
		formatExport : function() {
			return '导出数据';
		},
		formatClearFilters : function() {
			return '清空过滤';
		}
	};
	$
			.extend($.fn.bootstrapTable.defaults,
					$.fn.bootstrapTable.locales['zh-CN']);
})(jQuery);

var TableInit = function(URL, ID, THEAD, TYPE, SIZE) {
	var oTableInit = new Object();
	if (SIZE == undefined) {
		SIZE = 15;
	}
	// 初始化Table
	oTableInit.Init = function() {
		$('#btable').bootstrapTable({
			url : URL, // 请求后台的URL（*）
			method : TYPE, // 请求方式（*）
			toolbar : '#toolbar', // 工具按钮用哪个容器
			striped : true, // 是否显示行间隔色
			cache : false, // 是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
			sidePagination : "server", // 分页方式：client客户端分页，server服务端分页（*）
			pagination : true, // 是否显示分页（*）
			queryParamsType : '',
			align:'center',
			sortable : false,
			sortOrder : "asc", // 排序方式
			pageNumber : 1, // 初始化加载第一页，默认第一页
			pageSize : SIZE, // 每页的记录行数（*）
			pageList : [ 15, 20 ], // 可供选择的每页的行数（*）
			search : true, // 是否显示表格搜索，此搜索是客户端搜索，不会进服务端
			strictSearch : true,
			showColumns : true, // 是否显示所有的列
			showRefresh : true, // 是否显示刷新按钮
			showToggle : true,
			minimumCountColumns : 2, // 最少允许的列数
			clickToSelect : true, // 是否启用点击选中行
			// height: 500, //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
			uniqueId : ID, // 每一行的唯一标识，一般为主键列
			cardView : false, // 是否显示详细视图
			detailView : false, // 是否显示父子表
			columns : THEAD
		});
	};

	return oTableInit;
};

// 表格数据获取的参数
function queryParams(params) {
	return {
		pageSize : params.limit,
		pageNumber : params.offset,
		sortOrder : params.order,
	// status : searchBox.userName,
	// starDate : searchBox.userName,
	// endDate : searchBox.endDate
	}
}
function BootstrapTableInit(URL, ID, THEAD, TYPE, SIZE) {
	$("#btable").bootstrapTable('destroy');
	var oTable = new TableInit(URL, ID, THEAD, TYPE, SIZE);
	oTable.Init();
	$('#btable').bootstrapTable('hideColumn', ID);
	/* $("button[name='toggle']").hide(); */
}
