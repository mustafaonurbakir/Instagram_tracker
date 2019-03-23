import QtQuick 2.4
import QtQuick.Dialogs 1.2
import QtQuick.Controls 1.6
import QtQuick.Dialogs.qml 1.0
import QtQuick.Layouts 1.3
//import "qml"

ApplicationWindow {
    id: root
    visible: true
    title: "Instagram Tracker"
	
	property real degervarmi: 0

    MessageDialog {
        id: aboutDialog
        icon: StandardIcon.Information
        title: qsTr("About")
        text: "Instagram Tracker"
        informativeText: qsTr("This example made by ONUR.")
    }
	MessageDialog {
        id: secimyokDialog
        icon: StandardIcon.Warning
        title: qsTr("Secim yapmadin!")
        text: "Secim yapmadin!"
        informativeText: qsTr("1. Takip ettiplerin listesinden birini sec \n2. 'Takip listesine ekle' butonuna bas \n3. Asagida ki listeden birini sec")
    }

    Action {
        id: copyAction
        text: qsTr("&Copy")
        shortcut: StandardKey.Copy
        iconName: "edit-copy"
        enabled: (!!activeFocusItem && !!activeFocusItem["copy"])
        onTriggered: activeFocusItem.copy()
    }

    Action {
        id: cutAction
        text: qsTr("Cu&t")
        shortcut: StandardKey.Cut
        iconName: "edit-cut"
        enabled: (!!activeFocusItem && !!activeFocusItem["cut"])
        onTriggered: activeFocusItem.cut()
    }

    Action {
        id: pasteAction
        text: qsTr("&Paste")
        shortcut: StandardKey.Paste
        iconName: "edit-paste"
        enabled: (!!activeFocusItem && !!activeFocusItem["paste"])
        onTriggered: activeFocusItem.paste()
    }

    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")
            MenuItem {
                text: qsTr("E&xit")
                shortcut: StandardKey.Quit
                onTriggered: Qt.quit()
            }
        }
        Menu {
            title: qsTr("&Edit")
            MenuItem {
                action: cutAction
            }
            MenuItem {
                action: copyAction
            }
            MenuItem {
                action: pasteAction
            }
        }
        Menu {
            title: qsTr("&Help")
            MenuItem {
                text: qsTr("About...")
                onTriggered: aboutDialog.open()
            }
        }
    }

    MainForm {
        id: mainForm

        anchors.fill: parent

        Layout.minimumWidth: 800
        Layout.minimumHeight: 480
        Layout.preferredWidth: 1000
        Layout.preferredHeight: 600

    }
    function catchdata(aaaa,bbbb,cccc){
        //data python dosyasindan buraya gelebiliyor

    }

    function xxxx(){
		console.log("isthereproblem:")
		console.log(degervarmi)
		if(degervarmi===1){
			calculator.takedata()
		}
		else{
			secimyokDialog.open()
		}
    }

    function asagi_indir(){
        calculator.guncelleme()
    }

    Connections {
        target: calculator
		
		onPersontoTakeResult: {
			degervarmi = isthereproblem
		}
    }
}

/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
