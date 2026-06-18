
###### モジュール
import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import plotly.graph_objects as go




###### 関数

# category_optionsごとにグループ化してstatisticで選んだ統計量を出力
def make_columns(main_data,category_options,num_options,static,all_columns):
        
        select_all_columns = []
        select_all_columns.extend(category_options)
        select_all_columns.extend(num_options)
        drop_columns = [ i for i in all_columns if i not in select_all_columns]


        main_group_0 = main_data.drop(columns=drop_columns)

        if static == '合計':
            output_group = main_group_0.groupby(category_options,as_index=False).sum()
        elif static == '中央値':
            output_group = main_group_0.groupby(category_options,as_index=False).median()
        elif static == '平均値':
            output_group = main_group_0.groupby(category_options,as_index=False).mean()
        elif static == '最小値':
            output_group = main_group_0.groupby(category_options,as_index=False).min()
        elif static == '最大値':
            output_group = main_group_0.groupby(category_options,as_index=False).max()

        return output_group

#棒グラフを作成する関数
def show_graph(category_options,num_options,fig_data_group):
    # カテゴリ変数が複数ある場合
    if len(category_options) >= 2:
        # 数値尺度の数によってグラフを複数作る
        for i in range(0,len(num_options)): 
            # 棒グラフ作成
            fig_group = px.bar(
                fig_data_group, 
                x=category_options[0], 
                y=num_options[i], 
                color= category_options[1],
                text_auto=True,      # 棒の上に値を表示
                barmode = 'relative'
                    
            )

            # 3. Streamlitで表示
            st.plotly_chart(fig_group, use_container_width=True)

            

        # カテゴリ変数が一つの場合
    elif len(category_options) == 1:
        # 数値関数の数によって複数グラフを作る
        for i in range(0,len(num_options)):
            # 棒グラフ作成
            fig_group = px.bar(
                fig_data_group, 
                x=category_options[0], 
                y=num_options[i], 
                color= category_options[0],
                text_auto=True,      # 棒の上に値を表示
                barmode = 'relative'
                    
            )

                # 3. Streamlitで表示
            st.plotly_chart(fig_group, use_container_width=True)

            
    else:
        st.write('不具合が発生しております。ご不便をおかけし申し訳ございません')

# グラフと表を表示
def show_graph_and_table(category_options,num_options,statistic,data,all_columns):
    
    if len(category_options) >= 1 and len(num_options) >= 1 and len(statistic) >= 1:
        # グラフ作成用の表を作成する
        tips_group = make_columns(data,category_options,num_options,statistic,all_columns)
        # 作成した表を出力
        st.dataframe(tips_group)
        show_graph(category_options,num_options,tips_group)
    else:
        st.write('※指標を指定しないとグラフは表示されません')


# 時系列データをグラフ化
def time_series_graph(dataname,x_column,y_column):
    df = sns.load_dataset(dataname)
    # Date列を文字列から「日付型（datetime）」に変換（これが重要！）
    df["Date"] = pd.to_datetime(df["Date"])


# 3. Plotlyで時系列折れ線グラフを作成
    fig = px.line(
        df,
        x=x_column,
        y=y_column,
        
        
    )

    # 4. グラフの見た目の調整
    fig.update_layout(
        hovermode="x unified",  # ホバー時に日付と値をまとめて表示
    )
    fig.update_traces(
        line_color="#2b5c8f",   # 海をイメージしたブルーに変更
        line_width=1.5
    )

    # 5. 下部に期間調整のスライダー（レンジスライダー）を追加
    fig.update_xaxes(rangeslider_visible=True)

    # 6. Streamlitにグラフを表示
    st.plotly_chart(fig, use_container_width=True)

# anscombeグラフ用
def anscombe_graph():
    df = sns.load_dataset("anscombe")

    fig = px.scatter(
        df, 
        x="x", 
        y="y", 
        facet_col="dataset", 
        facet_col_wrap=2,  # 2列の格子状に並べる（4つのグラフが2×2になる）
        color="dataset",   # グループごとに色分け
        labels={"x": "X軸", "y": "Y軸", "dataset": "データセット"},
        title="データセットごとの散布図",
        template="plotly_white" # すっきりした白背景のテーマ
    )

    # グラフの見た目を少し調整（マージンやタイトルの配置など）
    fig.update_layout(
        height=600,
        showlegend=False # 色分けしているので凡例は非表示に
    )

    # 4. Streamlitでグラフを描写
    st.plotly_chart(fig, use_container_width=True)

# カテゴリ変数ごとに散布図を表示
def scatter_bycategory(data_name,num1,num2,category):
    df = sns.load_dataset(data_name)

    fig = px.scatter(
        df, 
        x=num1, 
        y=num2, 
        facet_col=category, 
        facet_col_wrap=2,  # 2列の格子状に並べる（4つのグラフが2×2になる）
        color=category,   # グループごとに色分け
        template="plotly_white" # すっきりした白背景のテーマ
    )

    # グラフの見た目を少し調整（マージンやタイトルの配置など）
    fig.update_layout(
        height=600,
        showlegend=False # 色分けしているので凡例は非表示に
    )

    # 4. Streamlitでグラフを描写
    st.plotly_chart(fig, use_container_width=True)


def scatter_bycategory_onegraph(data_name,num1,num2,category):
    df = sns.load_dataset(data_name)

    fig = px.scatter(
        df, 
        x=num1, 
        y=num2, 
        color=category,   # グループごとに色分け
        template="plotly_white" # すっきりした白背景のテーマ
    )

    # グラフの見た目を少し調整（マージンやタイトルの配置など）
    fig.update_layout(
        height=600,
        showlegend=False # 色分けしているので凡例は非表示に
    )

    # 4. Streamlitでグラフを描写
    st.plotly_chart(fig, use_container_width=True)

def scatters(data_name,num1,num2):
    df = sns.load_dataset(data_name)

    fig = px.scatter(
        df, 
        x=num1, 
        y=num2, 
        template="plotly_white" # すっきりした白背景のテーマ
    )

    # グラフの見た目を少し調整（マージンやタイトルの配置など）
    fig.update_layout(
        height=600,
        showlegend=False # 色分けしているので凡例は非表示に
    )

    # 4. Streamlitでグラフを描写
    st.plotly_chart(fig, use_container_width=True)

# flights用の時系列データ用グラフ
def flight_line_chart():

    # flightsデータ取得
    flights = sns.load_dataset("flights")

        # yearとmonthから日付列を作成
    flights["date"] = pd.to_datetime(
            flights["year"].astype(str) + "-" + flights["month"].astype(str)
        )

        # Plotlyで折れ線グラフ作成
    # グラフ作成
    fig = go.Figure()

    fig.add_trace(
    go.Scatter(
        x=flights["date"],
        y=flights["passengers"],
        mode="lines",
        name="Passengers"
        )
    )

    # 時間軸操作機能追加
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),  # 下部スライダー
            type="date"
        )
    )

    st.plotly_chart(fig, use_container_width=True)

def exercise_graph(category):
    df_exercise = sns.load_dataset("exercise") 

    # 2. 'time' カラムから ' min' を削除して int型 に変換
    # ※「 min」のようにスペースを含めて置換すると綺麗に数字だけが残ります
    df_exercise["time"] = df_exercise["time"].str.replace(" min", "", regex=False).astype(int)

    fig = px.scatter(
        df_exercise, 
        x="time", 
        y="pulse", 
        facet_col=category, 
        facet_col_wrap=2,  # 2列の格子状に並べる（4つのグラフが2×2になる）
        color=category,   # グループごとに色分け
        template="plotly_white" # すっきりした白背景のテーマ
    )

    # グラフの見た目を少し調整（マージンやタイトルの配置など）
    fig.update_layout(
        height=600,
        showlegend=False # 色分けしているので凡例は非表示に
    )

    # 4. Streamlitでグラフを描写
    st.plotly_chart(fig, use_container_width=True)



def line_graph_bycategory(datasource,metric):
    df = sns.load_dataset(datasource)



    # 2. グラフにする指標をユーザーが選択できるようにする
    

    # 3. Plotlyで時系列折れ線グラフを作成

    fig = px.line(
        df,
        x="Year",
        y=metric,
        color="Country",
        title=f"国別 {metric} の経年変化",
        labels={"Year": "年", "Spending_USD": "医療費 (USD)", "Life_Expectancy": "期待寿命 (年)", "Country": "国名"},
        markers=True # 各データ点にドットを表示して見やすくする
    )

    # 4. グラフのレイアウト調整
    fig.update_layout(
        hovermode="x unified",  # 同じ「年」のデータをホバー時に一括表示
        xaxis=dict(dtick=5)     # X軸（年）の目盛りを5年刻みにする
    )

    # 5. Streamlitにグラフを表示
    st.plotly_chart(fig, use_container_width=True)

def line_graph_healthexp(datasource,metric):
    df_0 = sns.load_dataset(datasource)
    df = df_0.drop(columns="Country").groupby('Year',as_index=False).mean()



    # 2. グラフにする指標をユーザーが選択できるようにする
    

    # 3. Plotlyで時系列折れ線グラフを作成

    fig = px.line(
        df,
        x="Year",
        y=metric,
        
        title=f"{metric} の経年変化",
        labels={"Year": "年", "Spending_USD": "医療費 (USD)", "Life_Expectancy": "期待寿命 (年)"},
        markers=True # 各データ点にドットを表示して見やすくする
    )

    # 4. グラフのレイアウト調整
    fig.update_layout(
        hovermode="x unified",  # 同じ「年」のデータをホバー時に一括表示
        xaxis=dict(dtick=5)     # X軸（年）の目盛りを5年刻みにする
    )

    # 5. Streamlitにグラフを表示
    st.plotly_chart(fig, use_container_width=True)