import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2


TakipEdenlerForm {
    id: form
	property string valuess: ""
	property variant stringList: valuess.split(',')
	
    function readData() {
		valuess = calculator.takeeklenenfollowers()
		//valuess : calculator.takedata()
		for (var i = 1; i < stringList.length; i=i+3){
			form.tableView.model.append({
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
