import QtQuick 2.4
import QtQuick.Dialogs 1.2
import QtQuick.Controls 1.6
import QtQuick.Dialogs.qml 1.0
import QtQuick.Layouts 1.3

MyTakipEdilenlerForm {
    id: form211

    property string valuess: ""
    property variant stringList: valuess.split(',')
    property string person_no: ""
    property string person_id: ""
    property string person_fullname: ""

    function readData() {
        valuess = calculator.takemyfollowings()
        for (var i = 1; i < stringList.length; i=i+3){
            form211.tableView333.model.append({
                                        sira: (((i-1)/3)+1),
                                        userno: stringList[i],
                                        userid: stringList[i+1],
                                        fullname: stringList[i+2]
                                    })
        }
    }

    function send(person_no, person_id, person_fullname) {
        calculator.takeperson(person_no, person_id, person_fullname)
    }

    Connections {
        target: calculator
    }

    function setvalue(){
        tableView333.selection.forEach( function(rowIndex) {
                                        person_no = form211.tableView333.model.get(tableView333.currentRow).userno
                                        person_id = form211.tableView333.model.get(tableView333.currentRow).userid
                                        person_fullname = form211.tableView333.model.get(tableView333.currentRow).fullname
                                        })
        //send(person_no, person_id, person_fullname)
        calculator.takepersontolist(person_no, person_id, person_fullname)
    }

    Timer {
        id: texttimer
        interval: 500
        repeat: true
        running: true
        triggeredOnStart: true
        onTriggered: setvalue()
    }

    Component.onCompleted:{
        readData()
    }


}

/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
