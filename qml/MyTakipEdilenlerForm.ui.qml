import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2
import QtQuick.Dialogs.qml 1.0

Item {
    id: content

    width: 1000
    height: 600
    property alias tableView333: tableView333

    TableView {
        id: tableView333

        property int columnWidth: width / 13
        height: 400

        anchors.fill: parent

        TableViewColumn {
            role: "sira"
            title: qsTr("#")
            width: tableView333.columnWidth
        }

        TableViewColumn {
            role: "userno"
            title: qsTr("User No")
            width: tableView333.columnWidth * 4
        }

        TableViewColumn {
            role: "userid"
            title: qsTr("User ID")
            width: tableView333.columnWidth * 4
        }

        TableViewColumn {
            role: "fullname"
            title: qsTr("Full Name")
            width: tableView333.columnWidth * 4
        }

        model: ListModel {
        }
    }
}
