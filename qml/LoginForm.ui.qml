import QtQuick 2.4
import QtQuick.Controls 1.6
import QtQuick.Dialogs.qml 1.0
import QtQuick.Layouts 1.3

Item {
    width: 1000
    height: 600

    property alias gr_button: gr_button
    property alias userId: userId
    property alias userPass: userPass

    ColumnLayout {
        id: columnLayout
        anchors.fill: parent
        Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter

        Image {
            Layout.rowSpan: 1
            sourceSize.width: 200
            sourceSize.height: 50
            Layout.alignment: Qt.AlignHCenter | Qt.AlignBottom
            source: "images/logo.instagram.png"
        }

        ColumnLayout {
            id: columnLayout1
            x: 449
            y: 249
            //x: 189
            width: 300
            height: 100
            anchors.verticalCenterOffset: -100
            Layout.alignment: Qt.AlignHCenter | Qt.AlignTop

            RowLayout {
                id: rowLayout
                width: 200
                height: 50
                spacing: 0
                Layout.preferredHeight: 0
                Layout.preferredWidth: 0
                Layout.alignment: Qt.AlignHCenter | Qt.AlignTop

                TextField {
                    id: userId
                    width: 200
                    height: 30
                    Layout.fillWidth: false
                    Layout.alignment: Qt.AlignLeft | Qt.AlignTop
                    placeholderText: qsTr("Kullanıcı Adı")
                }
            }

            RowLayout {
                id: rowLayout1
                width: 200
                height: 50
                spacing: 0
                Layout.alignment: Qt.AlignHCenter | Qt.AlignTop

                TextField {
                    id: userPass
                    y: 0
                    width: 200
                    height: 30
                    Layout.fillWidth: false
                    placeholderText: qsTr("Şifre")
                    echoMode: TextInput.Password
                }
            }

            Button {
                id: gr_button
                width: 200
                height: 30
                text: qsTr("Giriş")
                Layout.fillWidth: false
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            }
        }
    }
}

/*##^## Designer {
    D{i:2;anchors_height:100;anchors_width:100}
}
 ##^##*/
