import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2

TakipEdilenlerForm {
    id: form22
	
	property string valuess: ""
	property variant stringList: valuess.split(',')
	
    function readData() {
		valuess = calculator.takefollowings()
		for (var i = 1; i < stringList.length; i=i+3){
			form22.tableView.model.append({
										sira: (((i-1)/3)+1),
										userno: stringList[i],
										userid: stringList[i+1],
										fullname: stringList[i+2]
									})
		}
    }

    Connections {
        target: calculator
    }

    Component.onCompleted: readData()
}
