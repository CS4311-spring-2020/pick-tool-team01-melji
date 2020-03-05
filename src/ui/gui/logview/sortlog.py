class sortlogs:
    def sortlogs(self,gridlayout,columnofsort,number_of_widget_columns):
        i = 0
        while gridlayout.itemAt(i,columnofsort).widget() != None:
            a = i+1
            while gridlayout.itemAt(a,columnofsort).widget() != None: 
                if gridlayout.itemAt(a,columnofsort).widget() < gridlayout.itemAt(i,columnofsort).widget():
                    self.switch(gridlayout,i,a,number_of_widget_columns)


                    

    def switch(self,gridlayout,i,a,number_of_widget_columns):
        x = 0
        while x < number_of_widget_columns:
                widget_a = gridlayout.itemAt(i,x).widget()
                widget_b = gridlayout.itemAt(a,x).widget()
                gridlayout.addWidget(widget_a,a,x)
                gridlayout.addWidget(widget_a,i,x)
