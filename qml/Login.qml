import QtQuick 2.4
import QtQuick.Dialogs 1.2
import QtQuick.Controls 1.6
import QtQuick.Dialogs.qml 1.0
import QtQuick.Layouts 1.3

LoginForm {

    gr_button.onClicked: xxxx()
    property string valuess: ""
	property real login_success : 0
	
	MessageDialog {
        id: loginDialog
        icon: StandardIcon.Critical
        title: qsTr("Login unsuccessful")
        text: "Login unsuccessful"
        informativeText: qsTr("Please control your information. Try again!")
    }
	
    function xxxx(){
        login_success = calculator.sendMyInfo(userId.text, userPass.text)
        
		
		if (login_success === 0){
			loginDialog.open()
        }
		else{
			state11.visible = false
			state22.visible = true
		}
    }

    Connections {
        target: calculator
    }

}

