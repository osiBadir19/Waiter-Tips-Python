class WaiterTip:
    # TODO: import global modules 
    import pandas as pd
    import plotly.express as px

    
    
    def __init__(self, url: str):
        self.data_set = self.pd.read_csv(url)

         
    # TODO: machine learning model algorithm
    def waiter_tips_model(self, features):
        """
        :param features: a list of data related for prediction
        :return: a preidction of the expected tip
        """
        # modules to be used
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        import numpy as np

        def transform_to_ints(column, values_dict):
            self.data_set[column] = self.data_set[column].map(values_dict)

        # convert string values to digital values for easier use
        transform_to_ints('sex', {'Female': 0, 'Male': 1})
        transform_to_ints('smoker', {'No': 0, 'Yes': 1})
        transform_to_ints('day', {'Thur': 0, 'Fri': 1, 'Sat': 2, 'Sun': 3})
        transform_to_ints('time', {'Lunch': 0, 'Dinner': 1})

        # data splitting for x, and y
        x = np.array(self.data_set[["total_bill", "sex", "smoker", "day",
                          "time", "size"]])
        y = np.array(self.data_set['tip'])

        # test models
        xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(xtrain, ytrain)
        features = np.array(features)
        return model.predict(features)

       
    # TODO: features_ input
    def features_input(self):
        """
        opens a window to input the data to predict the tip
        """
        import tkinter as tk
        # window intiation
        wind = tk.Tk()
        wind.geometry('400x700+650+200')
        wind.title('Waiter Tips Prediction')
        features = []

        # top header
        tk.Label(wind, text='Waiter Tip Prediction Model', font='arial 28 bold').pack()
        # Labels and entrires
        labels = [tk.Label(wind, text='total bill'), tk.Label(wind, text='sex (F=0, M=1)'),
                  tk.Label(wind, text='smoker (Y=1, N=0)'), tk.Label(wind, text='day (Thur=0, Fri=1, Sat=2, Sun=3)'),
                  tk.Label(wind, text='time (Dinner=1, Lunch=0)'), tk.Label(wind, text='number of guests on table')]
        entries = [tk.Entry(wind), tk.Entry(wind), tk.Entry(wind), tk.Entry(wind), tk.Entry(wind), tk.Entry(wind)]

        for label, entry in zip(labels, entries):
            label.pack()
            entry.pack()

        def call_function():
            features.append([float(element.get()) for element in entries])
            print("the expected tip is :\n\t\t\t", self.waiter_tips_model(features))
            wind.destroy()

        tk.Button(wind, text='Predict Tip', command=call_function).pack()
        tk.mainloop()

        
    # TODO: figures and plotting data on chart
    def figure_data(self, depends_on: str, xaxis='total_bill'):
        """
        :param depends_on: the column that the calculations depnds on
        :param xaxis:
        :return: a graph
        """
        figure = self.px.scatter(data_frame=self.data_set, x=xaxis,
                                 y='tip', size='size', color=depends_on, trendline='ols')
        figure.show()   
  
  
    def pie_figure(self, values, names):
        """
        :param values: the values to calculate
        :param names: the names related to values
        :return: a pie graph
        """
        figure = self.px.pie(data_frame=self.data_set, values=values,
                             names=names)
        figure.show()

