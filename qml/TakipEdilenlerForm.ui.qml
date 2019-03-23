import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2

Item {
    id: content

    width: 640
    height: 400
    property alias tableView: tableView

    TableView {
        id: tableView

        property int columnWidth: width / 13
        height: 400

        anchors.fill: parent

		TableViewColumn {
            role: "sira"
            title: qsTr("#")
            width: tableView.columnWidth
        }
		
        TableViewColumn {
            role: "userno"
            title: qsTr("User No")
            width: tableView.columnWidth*4
        }

        TableViewColumn {
            role: "userid"
            title: qsTr("User ID")
            width: tableView.columnWidth*4
        }

        TableViewColumn {
            role: "fullname"
            title: qsTr("Full Name")
            width: tableView.columnWidth*4
        }

        model: ListModel {
        }
    }
}
