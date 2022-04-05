import statistics, random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)
print("Population mean is ", mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

stdev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("Sampling mean is ", mean)
print("Sampling Standard Deviation is ", stdev)

first_std_deviation_start, first_std_deviation_end = mean-stdev, mean+stdev
second_std_deviation_start, second_std_deviation_end = mean-(2*stdev), mean+(2*stdev)
third_std_deviation_start, third_std_deviation_end = mean-(3*stdev), mean+(3*stdev)

fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0,1], mode="lines", name="STD1START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0,1], mode="lines", name="STD1END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0,1], mode="lines", name="STD2START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0,1], mode="lines", name="STD2END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0,1], mode="lines", name="STD3START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0,1], mode="lines", name="STD3END"))
fig.show()

df2 = pd.read_csv("sample_2.csv")["reading_time"].tolist()
mean2 = statistics.mean(df2)
print("Mean of Sample1 is ", mean2)

fig2 = ff.create_distplot([mean_list], ["Student's Marks"], show_hist=False)
fig2.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = 'lines', name = "MEAN"))
fig2.add_trace(go.Scatter(x = [mean2, mean2], y = [0, 1], mode = 'lines', name = "SAMPLE MEAN"))
fig2.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0,1], mode="lines", name="STD1END"))
fig2.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0,1], mode="lines", name="STD2END"))
fig2.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0,1], mode="lines", name="STD3END"))
fig2.show()

z_score = (mean-mean2)/stdev
print("Z-Score found! Z-Score: ", z_score)