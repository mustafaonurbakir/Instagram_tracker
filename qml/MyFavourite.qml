import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2

MyFavouriteForm {
    id: form22

    property string valuess: ""
    property variant stringList: valuess.split(',')
    property string person_no: ""
    property string person_id: ""
    property string person_fullname: ""

    function readData() {
        valuess = calculator.takemyfavourite()
        console.log("values")
        console.log(valuess)
        for (var i = 1; i < stringList.length; i=i+3){
            form22.tableView277.model.append({
                                        sira: (((i-1)/3)+1),
                                        userno: stringList[i],
                                        userid: stringList[i+1],
                                        fullname: stringList[i+2]
                                    })
        }
    }
    //guncelleme
    function readData2() {
        valuess = calculator.takemyfavourite()
        console.log("values")
        console.log(valuess)
        for (var i = 1; i < stringList.length; i=i+3){
            form22.tableView277.model.append({
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
        tableView277.selection.forEach( function(rowIndex) {
                                        person_no = form22.tableView277.model.get(tableView277.currentRow).userno
                                        person_id = form22.tableView277.model.get(tableView277.currentRow).userid
                                        person_fullname = form22.tableView277.model.get(tableView277.currentRow).fullname
                                        })
        send(person_no, person_id, person_fullname)
    }

    Timer {
        id: texttimer
        interval: 500
        repeat: true
        running: true
        triggeredOnStart: true
        onTriggered: setvalue() & readData2()
    }

    Component.onCompleted:{
        readData()
    }
}


/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
