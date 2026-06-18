#### ライブラリ
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
# 内部モジュール
from viz_functions import make_columns,show_graph,show_graph_and_table,time_series_graph,scatter_bycategory,scatters,flight_line_chart,exercise_graph,line_graph_bycategory,scatter_bycategory_onegraph


# ヘッダー
st.header("Seaborn オープンデータ内容確認サイト")

st.write("seabornで提供されているデータの内容をグラフで確認するサイトです")

st.link_button("Seaborn提供データ詳細ページ","https://github.com/mwaskom/seaborn-data/tree/master")
st.write('\n')
# タブを作る
tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11,tab12,tab13,tab14,tab15,tab16,tab17,tab18,tab19,tab20,tab21= st.tabs([
                                    "Tips",
                                    "Titanic",
                                    "Anagrams",
                                    "Anscombe",
                                    "Attention",
                                    "Car_crashes",
                                    "Diamonds",
                                    "Dots",
                                    "Dowjones",
                                    "Exercise",
                                    "Flights",
                                    "fMRI",
                                    "Geyser",
                                    "Glue",
                                    "Healthexp",
                                    "Iris",
                                    "mpg",
                                    "Penguins",
                                    "Planets",
                                    "Seaice",
                                    "Taxis"
                                    ])

# カテゴリごとにグラフと統計量を表示するための統計量リスト
static_list = ['最大値','最小値','平均値','中央値','合計']


# Tipsデータタブ
with tab1:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.write('''
    あるウェイターがあるレストランで数ヶ月間勤務する間に受け取ったチップに関する情報を記録したデータです。 \n
    \n \n
    以下変数一覧です \n
    ・tip:ドルでのチップ \n
    ・total_bill:ドル建ての請求書 \n
    ・sex:請求書支払者の性別 \n
    ・smoker:パーティーに喫煙者がいたかどうか \n
    ・day:曜日 \n
    ・time:時間帯 \n
    ・size: パーティーの規模  \n \n \n


    ''')

    ### データを表示
    st.write(" \n \n ")
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn tipsデータ")
    
    # データを表示
    if st.button('データを表示する',key='tips_button' ):
        tips = sns.load_dataset("tips")
        st.dataframe(tips)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('tips')


    """,
        language="python",
    )

    st.write('\n \n ')
    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['total_bill','tip','size']
    )

    #カテゴリーを選択
    category_options = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['sex','smoker','day','time']
    )

    #統計量を決める
    statistic = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='tips_static_option'
    )

    all_columns_tips = ['total_bill','tip','size','sex','smoker','day','time']

    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='tips_stats_graph_button' ):
        tips = sns.load_dataset("tips")
        show_graph_and_table(category_options,num_options,statistic,tips,all_columns_tips)


    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_tips = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['total_bill','tip','size'],
        key='tips_scatter_x'
    )
    #y軸指標を選択
    num_options_y_tips = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['total_bill','tip','size'],
        key='tips_scatter_y'
    )

    #カテゴリーを選択
    category_options_tips = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['sex','smoker','day','time'],
        key='tips_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='tips_scatter_by_category_button' ):
        scatter_bycategory("tips",num_options_x_tips,num_options_y_tips,category_options_tips)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='tips_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("tips",num_options_x_tips,num_options_y_tips,category_options_tips)


# タイタニックデータタブ
with tab2:
    # データの概要
    st.subheader("データの概要")
    st.write('''
    タイタニック号の沈没事故で生存したかどうか、以下の変数で分類したデータになります。 \n
    \n \n
    以下変数一覧です \n
    ・alive:生存したかどうか(0=No,1=Yes) \n
    ・pclass:チケットクラス(1 = 1st, 2 = 2nd, 3 = 3rd)\n
    ・class:チケットクラス\n
    ・age:年齢 \n
    ・sex:性別 \n
    ・who:男女どっちか \n
    ・adult_male:成人男性がどうか \n
    ・sibsp:タイタニック号に乗船していた兄弟姉妹／配偶者の数 \n
    ・parch:タイタニック号に乗船していた親と子供の数 \n
    ・ticket:チケット番号 \n
    ・fare: 運賃  \n 
    ・ticket:チケット番号 \n
    ・cabin:船室番号 \n
    ・deck:乗船デッキ \n
    ・embarked:乗船港(C = シェルブール、Q = クイーンズタウン、S = サウサンプトン) \n \n \n

    ''')

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn titanicデータ")
    

    if st.button('データを表示する',key='titanic_button' ):
        titanic = sns.load_dataset("titanic")
        st.dataframe(titanic)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('titanic')


    """,
        language="python",
    )

    st.write('\n \n ')
    # グラフを表示
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_titanic = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['survived','age','parch','fare','sibsp'],
        key='titanic_num_option' 
    )

    #カテゴリーを選択
    category_options_taitanic = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['pclass','sex','embarked','class','adult_male','deck','embark_town','alive','alone','who'],
        key='titanic_category_option' 
    )

    #統計量を決める
    statistic_titanic = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='titanic_static_option' 
    )

    all_columns_titanic = ['survived','age','parch','fare','sibsp',
                           'pclass','sex','embarked','class','adult_male',
                           'deck','embark_town','alive','alone','who']


        
    # グラフと表を作成
    if st.button('統計量とグラフを表示する',key='titanic_stats_graph_button' ):
        titanic = sns.load_dataset("titanic")
        show_graph_and_table(category_options_taitanic,num_options_titanic,
                             statistic_titanic,titanic,all_columns_titanic)

    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_titanic = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['survived','age','parch','fare','sibsp'],
        key='titanic_scatter_x'
    )
    #y軸指標を選択
    num_options_y_titanic = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['survived','age','parch','fare','sibsp'],
        key='titanic_scatter_y'
    )

    #カテゴリーを選択
    category_options_titanic = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['pclass','sex','embarked','class','adult_male','deck','embark_town','alive','alone','who'],
        key='titanic_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='titanic_scatter_by_category_button' ):
        scatter_bycategory("titanic",num_options_x_titanic,num_options_y_titanic,category_options_titanic)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='titanic_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("titanic",num_options_x_titanic,num_options_y_titanic,category_options_titanic)



# Anagramデータタブ
with tab3:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.write('''
    このデータセットは20人の被験者が注意を分散(divided)または集中(focused)させながらアナグラムを学習する実験課題のデータです。 \n
    \n \n
    以下変数一覧です \n
    ・subidr:被験者ID \n
    ・attnr:注意の状態(「divided（分割）」と「focused（集中）」の2種類) \n
    ・num1:1分間でのアナグラム正解数 \n
    ・num2:2分間でのアナグラム正解数 \n
    ・num3:3分間でのアナグラム正解数 \n \n \n
  


    ''')

    ### データを表示
    st.subheader("データを表示")

    # データを表示
    st.write("seaborn anagramsデータ")
    if st.button('データを表示する',key='anagram_button' ):
        anagram = sns.load_dataset("anagrams")
        st.dataframe(anagram)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('anagrams')


    """,
        language="python",
    )

    st.write('\n \n ')
    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_anagram = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['num1','num2','num3'],
        key='anagram_num_options'
    )

    #カテゴリーを選択
    category_options_anagram = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['subidr','attnr'],
        key='anagram_category_options'
    )

    #統計量を決める
    statistic_anagram = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='anagram_statistic'
    )

    all_columns_anagram = ['subidr','attnr','num1','num2','num3']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='anagram_stats_graph_button' ):
        anagram = sns.load_dataset("anagrams")
        show_graph_and_table(category_options_anagram,num_options_anagram,
                             statistic_anagram,anagram,all_columns_anagram)

    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_anagram = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['num1','num2','num3'],
        key='anagram_scatter_x'
    )
    #y軸指標を選択
    num_options_y_anagram = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['num1','num2','num3'],
        key='anagram_scatter_y'
    )

    #カテゴリーを選択
    category_options_anagram = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['subidr','attnr'],
        key='anagram_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='anagram_scatter_by_category_button' ):
        scatter_bycategory("anagrams",num_options_x_anagram,num_options_y_anagram,category_options_anagram)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='anagram_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("anagrams",num_options_x_anagram,num_options_y_anagram,category_options_anagram)


# anscombeデータタブ
with tab4:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    このデータセットは、4つのグループ（I, II, III, IV）に分かれた、
    それぞれ11組ずつの $(x, y)$ のペア（合計44行）で構成されています。 \n
    最大のポイントは、4つのグループすべてにおいて、平均値、分散、相関係数、回帰直線などの「統計量」がほぼ完全に一致するという点です。
    しかし、実際にグラフ（散布図）を描いてみると、以下のように全く異なる形をしています。\n
    グループ I: 一般的な直線的な関係（線形関係）\n 
    グループ II: 綺麗な曲線（二次関数的な関係）\n 
    グループ III: 1点だけ外れ値がある直線関係 \n 
    グループ IV: x の値がほぼ一定だが、1点だけ離れた場所にある（外れ値の影響）\n\n\n
    <br>
    以下変数一覧です \n
    ・dataset:グループの名前 \n
    ・x:説明変数 \n
    ・y:目的変数 \n
    \n \n \n
  


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    ### データを表示
    st.write("seaborn ancombeデータ")
    

    ### データを表示
    if st.button('データを表示する',key='ansconbe_button' ):
        ansconbe = sns.load_dataset("anscombe")
        st.dataframe(ansconbe)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('anscombe')


    """,
        language="python",
    )

    st.write('\n \n ')

    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")

    #数値指標を選択
    num_options_ansconbe = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['x','y'],
        key='ansconbe_num_options'
    )

    #カテゴリーを選択
    category_options_ansconbe = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['dataset'],
        key='ansconbe_category_options'
    )

    #統計量を決める
    statistic_ansconbe = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='ansconbe_statistic'
    )

    all_columns_ansconbe = ['x','y','dataset']

    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='anscombe_stats_graph_button' ):
        ansconbe = sns.load_dataset("anscombe")
        show_graph_and_table(category_options_ansconbe,num_options_ansconbe,
                             statistic_ansconbe,ansconbe,all_columns_ansconbe)


    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_ansconbe = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['x','y'],
        key='ansconbe_scatter_x'
    )
    #y軸指標を選択
    num_options_y_ansconbe = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['x','y'],
        key='ansconbe_scatter_y'
    )

    #カテゴリーを選択
    category_options_ansconbe = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['dataset'],
        key='ansconbe_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='ansconbe_scatter_by_category_button' ):
        scatter_bycategory("anscombe",num_options_x_ansconbe,num_options_y_ansconbe,category_options_ansconbe)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='anscombe_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("anscombe",num_options_x_ansconbe,num_options_y_ansconbe,category_options_ansconbe)


# attentionデータタブ
with tab5:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    このデータセットは、心理学や認知科学の実験データを模したデータセットです。\n
    「注意の集中度合い」と「タスクの難易度（解の数）」という2つの要素が、
    最終的な「テストの成績（スコア）」にどのような影響を与えるか、
    そしてそれらがどう相互に作用しているかを分析するために作られています。 \n
    \n\n\n
    以下変数一覧です \n
    ・Unnamed: 0:行のインデックス（通し番号） \n
    ・subject:被験者ID \n
    ・attention:注意の状態。(divided:他に気を取られている状態,focused:タスクに没頭している状態)\n
    ・solutions:問題の難易度(スクの複雑さを表しており、1,2,3 の3段階がある) \n
    ・score:テストの得点（スコア） \n
    \n \n \n
  


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    ### データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn attentionデータ")
    

    # データを表示
    if st.button('データを表示する',key='attention_button' ):
        attention = sns.load_dataset("attention")
        st.dataframe(attention)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('attention')


    """,
        language="python",
    )

    st.write('\n \n ')
    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_attention = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['solutions','score'],
        key='attention_num_options'
    )

    #カテゴリーを選択
    category_options_attention = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['Unnamed: 0','subject','attention'],
        key='attention_category_options'
    )

    #統計量を決める
    statistic_attention = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='attention_statistic'
    )

    all_columns_attention = ['solutions','score','Unnamed: 0','subject','attention']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='attention_stats_graph_button' ):
        attention = sns.load_dataset("attention")
        show_graph_and_table(category_options_attention,num_options_attention,
                             statistic_attention,attention,all_columns_attention)


    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_attention = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['solutions','score'],
        key='attention_scatter_x'
    )
    #y軸指標を選択
    num_options_y_attention = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['solutions','score'],
        key='attention_scatter_y'
    )

    #カテゴリーを選択
    category_options_attention = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['subject','attention'],
        key='attention_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='attention_scatter_by_category_button' ):
        scatter_bycategory("attention",num_options_x_attention,num_options_y_attention,category_options_attention)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='attention_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("attention",num_options_x_attention,num_options_y_attention,category_options_attention)

# car crashesデータ
with tab6:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    このデータセットはアメリカの各州における自動車事故の統計データをまとめたものです。\n
    主に、事故の発生率（死亡事故数）と、その背景にある原因（スピード出しすぎ、アルコール、居眠りなど）や、
    保険会社に関わる経済的なデータ（保険料、保険会社の損失額）との関係性が記録されています。 \n
    \n\n\n
    以下変数一覧です \n
    ・total:10億マイル走行あたりの運転者死亡事故数（全体の事故率の指標） \n
    ・speeding:スピードの出しすぎが原因の死亡事故数（10億マイルあたり） \n
    ・alcohol:アルコール（飲酒運転）が原因の死亡事故数（10億マイルあたり） \n
    ・not_distracted:脇見・上の空（不注意）ではなかった死亡事故数（10億マイルあたり） \n
    ・no_previous:過去に事故歴がないドライバーによる死亡事故数（10億マイルあたり） \n
    ・ins_premium:自動車保険の平均年間保険料（ドル） \n
    ・ins_losses:保険会社が被ったドライバー1人あたりの平均損失額（ドル） \n
    ・abbrev:州名の略称（例: AL = アラバマ州、CA = カリフォルニア州など） \n
    \n \n \n
  


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn car_crashesデータ")
    

    # データを表示
    if st.button('データを表示する',key='car_crashes_button' ):
        car_crashes = sns.load_dataset("car_crashes")
        st.dataframe(car_crashes)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('car_crashes')


    """,
        language="python",
    )

    st.write('\n \n ')
    # グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_car_crashes  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['total','speeding','alcohol','not_distracted','no_previous','ins_premium','ins_losses'],
        key='car_crashes_num_options'
    )

    #カテゴリーを選択
    category_options_car_crashes = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['abbrev'],
        key='car_crashes_category_options'
    )

    #統計量を決める
    statistic_car_crashes = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='car_crashes_statistic'
    )

    all_columns_car_crashes = ['total','speeding','alcohol','not_distracted',
                               'no_previous','ins_premium','ins_losses','abbrev']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='car_crashes_stats_graph_button' ):
        car_crashes = sns.load_dataset("car_crashes")
        show_graph_and_table(category_options_car_crashes,num_options_car_crashes,
                             statistic_car_crashes,car_crashes,all_columns_car_crashes)

    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("散布図を表示")
    #x軸指標を選択
    num_options_x_car_crashes = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['total','speeding','alcohol','not_distracted','no_previous','ins_premium','ins_losses'],
        key='car_crashes_scatter_x'
    )
    #y軸指標を選択
    num_options_y_car_crashes = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['total','speeding','alcohol','not_distracted','no_previous','ins_premium','ins_losses'],
        key='car_crashes_scatter_y'
    )

    if st.button('グラフを表示する',key='car_crashes_scatter_by_category_button' ):
        scatters("car_crashes",num_options_x_car_crashes,num_options_y_car_crashes)

    
    
    


# Diamondsデータ
with tab7:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    このデータセットは約54,000個のダイヤモンドの価格や品質、サイズに関するデータをまとめたものです。\n
    ダイヤモンドの価値を決める「4C」（Carat, Cut, Color, Clarity）に加えて、実測サイズや価格が含まれています。 \n
    \n\n\n
    以下変数一覧です \n
    ・carat:カラット。ダイヤモンドの重さ(1カラット=0.2グラム) \n
    ・cut:カットの輝き(品質)。(悪い順に Fair ➔ Good ➔ Very Good ➔ Premium ➔ Ideal) \n
    ・color:ダイヤモンドの色。J(最悪:わずかに黄色)からD(最高:完全無色)までの7段階 \n
    ・clarity:透明度。(悪い順にI1➔SI2➔SI1➔VS2➔VS1➔VVS2➔VVS1➔IF)\n
    ・depth:総深さ比率（％）。計算式は $2z / (x + y)$。全体の高さが幅に対して何％か \n
    ・table:テーブル比率（％）。ダイヤモンドの真上にある最も広い平らな面の幅（比率）\n
    ・price:価格（米ドル）。 \n
    ・x:長さ（mm）。ダイヤモンドの平面的なサイズ（縦） \n
    ・y:幅（mm）。ダイヤモンドの平面的なサイズ（横） \n
    ・z:深さ（mm）。ダイヤモンドの厚み（高さ） \n
    \n \n \n
  


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn diamondsデータ")
    

    # データを表示
    if st.button('データを表示する',key='diamonds_button' ):
        diamonds = sns.load_dataset("diamonds")
        st.dataframe(diamonds)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('diamonds')


    """,
        language="python",
    )

    st.write('\n \n ')
    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_diamonds  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['carat','depth','price','table','x','y','z'],
        key='diamonds_num_options'
    )

    #カテゴリーを選択
    category_options_diamonds = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['cut','color','clarity'],
        key='diamonds_category_options'
    )

    #統計量を決める
    statistic_diamonds = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='diamonds_statistic'
    )

    all_columns_diamonds = ['carat','depth','price','table','x','y','z','cut','color','clarity']

    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='diamonds_stats_graph_button' ):
        diamonds = sns.load_dataset("diamonds")
        show_graph_and_table(category_options_diamonds,num_options_diamonds,
                             statistic_diamonds,diamonds,all_columns_diamonds)
    
    



    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_diamonds = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['carat','depth','price','table','x','y','z'],
        key='diamonds_scatter_x'
    )
    #y軸指標を選択
    num_options_y_diamonds = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['carat','depth','price','table','x','y','z'],
        key='diamonds_scatter_y'
    )

    #カテゴリーを選択
    category_options_diamonds = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['cut','color','clarity'],
        key='diamonds_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='diamonds_scatter_by_category_button' ):
        scatter_bycategory("diamonds",num_options_x_diamonds,num_options_y_diamonds,category_options_diamonds)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='diamonds_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("diamonds",num_options_x_diamonds,num_options_y_diamonds,category_options_diamonds)




# Dotsデータ
with tab8:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    このデータセットは神経科学（脳科学）における実験データをまとめたデータセットです。\n
    具体的には、サルやマウスなどの被験体に「動く無数の点（dots）」を見せ、
    その点がどちらの方向に動いているかを判断させるタスク（視覚的意志決定タスク）を行っている最中の、
    脳内の特定の神経細胞（ニューロン）の活動記録（発火頻度）が収められています。 \n
    \n\n\n
    以下変数一覧です \n
    ・align:時間の基準点。\n
            dots:画面に動く点（ドット）が表示された瞬間が基準（0）
            sacc: 被験体が目を動かして回答（サッカード）した瞬間が基準（0）\n
    ・choice:被験体の選択結果。\n
            T1 または T2 の2種類（例：右に動いたか、左に動いたかなどの選択肢に対応）\n
    ・time:align で指定された基準点からの経過時間(ミリ秒) \n
    ・coherence:点の動きの一貫性（％）。\n
            画面上のドットがどれだけ同じ方向へ綺麗に揃って動いているか（タスクの簡単さ）\n
    ・firing_rate:ニューロンの発火頻度（回/秒）。神経細胞が1秒間に何回電気信号を出したか \n

    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn dotsデータ")
    

    #### データを表示
    if st.button('データを表示する',key='dots_button' ):
        dots = sns.load_dataset("dots")
        st.dataframe(dots)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('dots')


    """,
        language="python",
    )

    st.write('\n \n ')
    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_dots  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['time','coherence','firing_rate'],
        key='dots_num_options'
    )

    #カテゴリーを選択
    category_options_dots = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['align','choice'],
        key='dots_category_options'
    )

    #統計量を決める
    statistic_dots = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='dots_statistic'
    )

    all_columns_dots = ['time','coherence','firing_rate','align','choice']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='dots_stats_graph_button' ):
        dots = sns.load_dataset("dots")
        show_graph_and_table(category_options_dots,num_options_dots,
                             statistic_dots,dots,all_columns_dots)


    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_dots = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['time','coherence','firing_rate'],
        key='dots_scatter_x'
    )
    #y軸指標を選択
    num_options_y_dots = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['time','coherence','firing_rate'],
        key='dots_scatter_y'
    )

    #カテゴリーを選択
    category_options_dots = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['align','choice'],
        key='dots_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='dots_scatter_by_category_button' ):
        scatter_bycategory("dots",num_options_x_dots,num_options_y_dots,category_options_dots)
    
    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='dots_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("dots",num_options_x_dots,num_options_y_dots,category_options_dots)



# Dowjonesデータ (グラフの機能要修正)
with tab9:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    dowjones（ダウ・ジョーンズ）は、アメリカの代表的な株価指数である
    「ダウ・ジョーンズ工業株価平均（Dow Jones Industrial Average: DJIA）」の歴史的な時系列データです。\n
    このデータセットは、1914年から1968年までの約50年間にわたるダウ平均株価の推移を記録しています。 \n
    \n\n\n
    以下変数一覧です \n
    ・Date:株価が記録された日付。フォーマットは YYYY-MM-DD（年-月-日）\n
    ・Price:その日付時点でのダウ平均株価（終値）。単位は米ドル（USD）\n
    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn dowjonesデータ")
    

    # データを表示
    if st.button('データを表示する',key='dowjones_button' ):
        dowjones = sns.load_dataset("dowjones")
        st.dataframe(dowjones)
    
    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('dowjones')


    """,
        language="python",
    )

    st.write('\n \n ')
    # グラフを表示のサブヘッダー
    st.subheader("時系列のグラフを表示")
    if st.button('グラフを表示する',key='dowjones_graph_button' ):
        time_series_graph("dowjones","Date","Price")



# Exerciseデータ
with tab10:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    このデータセットは、30人の被験者が「1分間」「15分間」「30分間」という
    異なる運動時間を経た際の心拍数を記録したものです。 \n
    \n\n\n
    以下変数一覧です \n
    ・Unnamed: 0:行のインデックス（通し番号）\n
    ・id:被験者ID \n
    ・diet:食事の条件（ダイエット条件）\n
        no fat: 脂肪分を抜いた食事
        low fat: 低脂肪の食事 \n
    ・pulse:心拍数（拍/分） \n
    ・time:運動をしていた時間。 \n
    ・kind:運動の種類。 \n
        rest: 安静（運動していない状態）
        walking: ウォーキング（軽い運動）
        running: ランニング（激しい運動）
    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn exerciseデータ")
    

    ### データを表示
    if st.button('データを表示する',key='exercise_button' ):
        exercise = sns.load_dataset("exercise")
        st.dataframe(exercise)
    
    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('exercise')


    """,
        language="python",
    )

    st.write('\n \n ')
    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_exercise  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['pulse'],
        key='exercise_num_options'
    )

    #カテゴリーを選択
    category_options_exercise = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['Unnamed: 0','id','diet','time','kind'],
        key='exercise_category_options'
    )

    #統計量を決める
    statistic_exercise = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='exercise_statistic'
    )

    all_columns_exercise = ['pulse','Unnamed: 0','id','diet','time','kind']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='exercise_stats_graph_button' ):
        exercise = sns.load_dataset("exercise")
        show_graph_and_table(category_options_exercise,num_options_exercise,
                             statistic_exercise,exercise,all_columns_exercise)

    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")

    #カテゴリーを選択
    category_options_exercise = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['diet','kind'],
        key='exercise_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='exercise_scatter_by_category_button' ):
        exercise_graph(category_options_exercise)
    
    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='exercise_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("exercise",'time','pulse',category_options_exercise)

# Flightsデータ(グラフの機能要修正)
with tab11:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    flights（フライト）は、1949年から1960年までの月別の国際航空旅客数を記録したクラシックな時系列データセットです。 \n
    \n\n\n
    以下変数一覧です \n
    ・year:年。1949から1960までの西暦を記録\n
    ・id:被験者ID \n
    ・month:月。Jan（1月）から Dec（12月）まで英語の略称で記録\n
    ・passengers:航空旅客数（千人単位） \n
    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn flightsデータ")
    

    # データを表示
    if st.button('データを表示する',key='flights_button' ):
        flights = sns.load_dataset("flights")
        st.dataframe(flights)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('flights')


    """,
        language="python",
    )

    st.write('\n \n ')
    # グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_flights  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['passengers'],
        key='flights_num_options'
    )

    #カテゴリーを選択
    category_options_flights = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['year','month'],
        key='flights_category_options'
    )

    #統計量を決める
    statistic_flights = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='flights_statistic'
    )

    all_columns_flights = ['year','month','passengers']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='flights_stats_graph_button' ):
        flights = sns.load_dataset("flights")
        show_graph_and_table(category_options_flights,num_options_flights,
                             statistic_flights,flights,all_columns_flights)


    ### 時系列グラフを表示
    st.write('\n \n ')
    st.subheader("時系列の乗客数を可視化")
    if st.button('グラフを表示する',key='flights_line_graph_button' ):
        flight_line_chart()


# fMRIデータ (他のグラフも追加)
with tab12:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    このデータセットは、脳科学・神経科学の実験データをまとめた時系列データセットです。 \n
    fMRI(機能的磁気共鳴画像法)を使って、被験者が特定のタスク（刺激）を行っているときの脳の活動（血流の変化）を
    時間経過とともに測定したデータです。\n
    14人の被験者（subject）が「刺激（stim）」または「視覚的な手がかり（cue）」を与えられた際に、
    脳の特定の領域（parietal：頭頂葉、frontal：前頭葉）で起こった血流の応答変化（BOLD信号）を時系列で記録したものです。 
    \n\n\n
    以下変数一覧です \n
    ・subject:被験者ID。s0 から s13 までの計14人の被験者を識別するためのID\n
    ・timepoint:時間軸(タイムポイント)。刺激が始まってからの経過時間(0から18のステップ) \n
    ・event:実験イベント（条件） \n
            stim: 実際に刺激が与えられている状態
            cue: 刺激の合図（手がかり）が出されている状態\n
    ・region:測定した脳の領域。\n
            parietal: 頭頂葉（空間認識や感覚処理に関わる部位）
            frontal: 前頭葉（思考や意思決定、運動に関わる部位） \n
    ・signal:BOLD信号の変動値(%)。(血液中の酸素量の変化を反映) \n
    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn fMRIデータ")
    

    ### データを表示
    if st.button('データを表示する',key='fmri_button' ):
        fmri = sns.load_dataset("fmri")
        st.dataframe(fmri)
    
    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('fmri')


    """,
        language="python",
    )

    st.write('\n \n ')
    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_fmri  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['timepoint','signal'],
        key='fmri_num_options'
    )

    #カテゴリーを選択
    category_options_fmri = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['subject','event','region'],
        key='fmri_category_options'
    )

    #統計量を決める
    statistic_fmri = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='fmri_statistic'
    )

    all_columns_fmri = ['timepoint','signal','subject','event','region']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='fmri_stats_graph_button' ):
        fmri = sns.load_dataset("fmri")
        show_graph_and_table(category_options_fmri,num_options_fmri,statistic_fmri,fmri,all_columns_fmri)


    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_fmri = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['timepoint','signal'],
        key='fmri_scatter_x'
    )
    #y軸指標を選択
    num_options_y_fmri = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['timepoint','signal'],
        key='fmri_scatter_y'
    )

    #カテゴリーを選択
    category_options_fmri = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['subject','event','region'],
        key='fmri_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='fmri_scatter_by_category_button' ):
        scatter_bycategory("fmri",num_options_x_fmri,num_options_y_fmri,category_options_fmri)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='fmri_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("fmri",num_options_x_fmri,num_options_y_fmri,category_options_fmri)


# geyserデータ 
with tab13:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    geyser（ガイザー）は、アメリカのイエローストーン国立公園にある有名な間欠泉（一定周期で水や熱湯を噴き出す温泉）
    「オールド・フェイスフル・ガイザー（Old Faithful Geyser）」の噴火に関する観測データです。 \n
    
    \n\n\n
    以下変数一覧です \n
    ・duration:噴火の継続時間（分）。一回の噴火が何分間続いたか\n
    ・waiting:次の噴火までの待ち時間（分） \n
    ・kind:噴火のパターンの分類。 \n
            継続時間の長さによって、自動的に long（長い）または short（短い）のどちらかに分類

    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn geyserデータ")
    

    ### データを表示
    if st.button('データを表示する',key='geyser_button' ):
        geyser = sns.load_dataset("geyser")
        st.dataframe(geyser)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('geyser')


    """,
        language="python",
    )

    st.write('\n \n ')
    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_geyser  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['duration','waiting'],
        key='geyser_num_options'
    )

    #カテゴリーを選択
    category_options_geyser = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['kind'],
        key='geyser_category_options'
    )

    #統計量を決める
    statistic_geyser = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='geyser_statistic'
    )

    all_columns_geyser = ['duration','waiting','kind']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='geyser_stats_graph_button' ):
        geyser = sns.load_dataset("geyser")
        show_graph_and_table(category_options_geyser,num_options_geyser,
                             statistic_geyser,geyser,all_columns_geyser)


    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_geyser = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['duration','waiting'],
        key='geyser_scatter_x'
    )
    #y軸指標を選択
    num_options_y_geyser = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['duration','waiting'],
        key='geyser_scatter_y'
    )

    #カテゴリーを選択
    category_options_geyser = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['kind'],
        key='geyser_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='geyser_scatter_by_category_button' ):
        scatter_bycategory("geyser",num_options_x_geyser,num_options_y_geyser,category_options_geyser)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='geyser_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("geyser",num_options_x_geyser,num_options_y_geyser,category_options_geyser)



# glueデータ (グラフ追加要検討)
with tab14:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    glue は、自然言語処理（NLP）AIモデルの評価ベンチマーク
    「GLUE（General Language Understanding Evaluation）」の結果をまとめたデータセットです。\n
    AI（特にBERTやT5、GPTの基盤となったTransformerなど）のモデルが、
    様々な言語理解タスクにおいてどれだけのスコア（成績）を収めたかが記録されています。 \n
    
    \n\n\n
    以下変数一覧です \n
    ・Model:AIモデルの名前\n
    ・year:モデルが発表された（またはデータが計測された）西暦年 \n
    ・Encoder:モデルが採用しているテキストの符号化技術（アーキテクチャ） \n
    ・Task:GLUEベンチマーク内で行われた言語タスク（テスト）の名前。 \n
            ・CoLA: 文法的な正しさを判定するタスク
            ・SST-2: 映画のレビューなどの感情分析（ポジティブ／ネガティブ）を行うタスク
            ・MRPC / QQP: 2つの文が同じ意味かどうかを判定するタスク
            ・STS-B: 2つの文の類似度をスコア化するタスク
            ・MNLI / RTE / WNLI: 含意関係（ある文から別の文が論理的に導き出せるか）を判定するタスク
            ・QNLI: 質問と文のペアから、回答が含まれているかを判定するタスク
    ・Score:各タスクでのモデルの正解率や評価スコア（0〜100の基準） \n

    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn glueデータ")
    

    # データを表示
    if st.button('データを表示する',key='glue_button' ):
        glue = sns.load_dataset("glue")
        st.dataframe(glue)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('glue')


    """,
        language="python",
    )

    st.write('\n \n ')
    # グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_glue  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['Score'],
        key='glue_num_options'
    )

    #カテゴリーを選択
    category_options_glue = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['Model','Year','Encoder','Task'],
        key='glue_category_options'
    )

    #統計量を決める
    statistic_glue = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='glue_statistic'
    )

    all_columns_glue = ['Model','Year','Encoder','Task','Score']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='glue_stats_graph_button' ):
        glue = sns.load_dataset("glue")
        show_graph_and_table(category_options_glue,num_options_glue,statistic_glue,glue,all_columns_glue)

# healthexpデータ (グラフ追加要検討)
with tab15:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    healthexpは世界主要国における医療費の支出額と、その国の平均寿命の歴史的推移をまとめたデータセットです。
    国の経済的な豊かさ（医療への投資額）が、国民の健康（寿命）にどう結びついているかをマクロ視点で分析するのに適しています。\n
    このデータセットには、日本、アメリカ、ドイツ、フランス、イギリス、カナダなどの先進国における、
    1970年から2020年（または2021年）までのデータが記録されています。
    
    \n\n\n
    以下変数一覧です \n
    ・Year:測定された西暦年\n
    ・Country:国名 \n
    ・Spending_USD:1人あたりの年間医療費（米ドル単位） \n
            インフレや購買力平価（PPP）を考慮して調整された、実質的な医療への投資額
    ・Life_Expectancy:平均寿命（歳） \n


    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    ### データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn healthexpデータ")
    

    ### データを表示
    if st.button('データを表示する',key='healthexp_button' ):
        healthexp = sns.load_dataset("healthexp")
        st.dataframe(healthexp)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('healthexp')


    """,
        language="python",
    )

    st.write('\n \n ')
    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_healthexp  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['Spending_USD','Life_Expectancy'],
        key='healthexp_num_options'
    )

    #カテゴリーを選択
    category_options_healthexp = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['Country','Year'],
        key='healthexp_category_options'
    )

    #統計量を決める
    statistic_healthexp = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='healthexp_statistic'
    )

    all_columns_healthexp = ['Spending_USD','Life_Expectancy','Country','Year']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='healthexp_stats_graph_button' ):
        healthexp = sns.load_dataset("healthexp")
        show_graph_and_table(category_options_healthexp,num_options_healthexp,
                             statistic_healthexp,healthexp,all_columns_healthexp)

    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_healthexp = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['Spending_USD','Life_Expectancy'],
        key='healthexp_scatter_x'
    )
    #y軸指標を選択
    num_options_y_healthexp = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['Spending_USD','Life_Expectancy'],
        key='healthexp_scatter_y'
    )

    #カテゴリーを選択
    category_options_healthexp = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['Country'],
        key='healthexp_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='healthexp_scatter_by_category_button' ):
        scatter_bycategory("healthexp",num_options_x_healthexp,num_options_y_healthexp,category_options_healthexp)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='healthexp_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("healthexp",num_options_x_healthexp,num_options_y_healthexp,category_options_healthexp)


    ### カテゴリーごとに散布図を表示
    st.write(" \n \n")
    st.subheader("カテゴリー変数ごとに時系列グラフを表示")

    healthexp_metric = st.selectbox(
        "表示する指標を選択してください",
        options=["Life_Expectancy", "Spending_USD"],
        format_func=lambda x: "Life_Expectancy" if x == "Life_Expectancy" else "Spending_USD"
    )

    if st.button('グラフを表示する',key='healthexp_line_graph_by_category_button' ):
        line_graph_bycategory("healthexp",healthexp_metric)


# irisデータ (グラフ追加要検討)
with tab16:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    iris（アイリス）は、3種類のアヤメ（花）の計測データをまとめたデータセットです。\n
    このデータセットは、3種類のアヤメ（Setosa, Versicolor, Virginica）について、
    それぞれ50個体ずつ（合計150行）の「がく（萼）」と「花びら（花弁）」の長さと幅を記録したものです。\n
    
    
    \n\n\n
    以下変数一覧です \n
    ・sepal_length:がく片（萼）の長さ\n
    ・sepal_width:がく片（萼）の幅 \n
    ・petal_length:花びら（花弁）の長さ \n
    ・petal_width:花びら（花弁）の幅 \n
    ・species:アヤメの品種（クラス） \n


    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn irisデータ")
    

    # データを表示
    if st.button('データを表示する',key='iris_button' ):
        iris = sns.load_dataset("iris")
        st.dataframe(iris)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('iris')


    """,
        language="python",
    )

    st.write('\n \n ')
    # グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_iris  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['sepal_length','sepal_width','petal_length','petal_width'],
        key='iris_num_options'
    )

    #カテゴリーを選択
    category_options_iris = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['species'],
        key='iris_category_options'
    )

    #統計量を決める
    statistic_iris = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='iris_statistic'
    )

    all_columns_iris = ['sepal_length','sepal_width','petal_length','petal_width','species']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='iris_stats_graph_button' ):
        iris = sns.load_dataset("iris")
        show_graph_and_table(category_options_iris,num_options_iris,statistic_iris,iris,all_columns_iris)

    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_iris = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['sepal_length','sepal_width','petal_length','petal_width'],
        key='iris_scatter_x'
    )
    #y軸指標を選択
    num_options_y_iris = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['sepal_length','sepal_width','petal_length','petal_width'],
        key='iris_scatter_y'
    )

    #カテゴリーを選択
    category_options_iris = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['species'],
        key='iris_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='iris_scatter_by_category_button' ):
        scatter_bycategory("iris",num_options_x_iris,num_options_y_iris,category_options_iris)
    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='iris_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("iris",num_options_x_iris,num_options_y_iris,category_options_iris)

    




# mgpデータ (グラフ追加要検討)
with tab17:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    mpgは1970年から1982年までに製造されたさまざまな自動車の燃費（マイル・パー・ガロン）や各種スペックをまとめたデータセットです\n
    自動車の重量、馬力、排気量などの物理的なスペックが、車の燃費にどのような影響を与えるかを分析・予測するためのデータとして、
    統計学や機械学習の回帰分析（価格や燃費の予測）の入門用に広く使われています。\n
    
    
    \n\n\n
    以下変数一覧です \n
    ・mpg:燃費(Miles Per Gallon)。1ガロンの燃料で何マイル走れるか\n
    ・cylinders:エンジンの気筒数（シリンダー数） \n
    ・displacement:エンジンの総排気量（キュービックインチ単位） \n
    ・acceleration:加速性能。静止状態から時速60マイル（約96.5km/h）に達するまでの時間（秒） \n
    ・model_year:製造年（西暦の下2桁） \n
    ・origin:製造地域（国） \n
    ・name:車種名（自動車のモデル名） \n


    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn mpgデータ")
    

    # データを表示
    if st.button('データを表示する',key='mgp_button' ):
        mgp = sns.load_dataset("mpg")
        st.dataframe(mgp)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('mpg')


    """,
        language="python",
    )

    st.write('\n \n ')
    # グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_mgp  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['mpg','cylinders','displacement','horsepower','weight','acceleration','model_year'],
        key='mgp_num_options'
    )

    #カテゴリーを選択
    category_options_mgp = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['origin','name'],
        key='mgp_category_options'
    )

    #統計量を決める
    statistic_mgp = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='mgp_statistic'
    )

    all_columns_mgp = ['mpg','cylinders','displacement','horsepower','weight',
                       'acceleration','model_year','origin','name']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='mpg_stats_graph_button' ):
        mgp = sns.load_dataset("mpg")
        show_graph_and_table(category_options_mgp,num_options_mgp,statistic_mgp,mgp,all_columns_mgp)

    
    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_mpg = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['mpg','cylinders','displacement','horsepower','weight','acceleration','model_year'],
        key='mpg_scatter_x'
    )
    #y軸指標を選択
    num_options_y_mpg = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['mpg','cylinders','displacement','horsepower','weight','acceleration','model_year'],
        key='mpg_scatter_y'
    )

    #カテゴリーを選択
    category_options_mpg = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['origin'],
        key='mpg_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='mpg_scatter_by_category_button' ):
        scatter_bycategory("mpg",num_options_x_mpg,num_options_y_mpg,category_options_mpg)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='mpg_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("mpg",num_options_x_mpg,num_options_y_mpg,category_options_mpg)




# penguinsデータ (グラフ追加要検討)
with tab18:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    penguinsは南極の島々に生息する3種類のペンギンの身体測定データをまとめたデータセットです \n
    
    
    
    \n\n\n
    以下変数一覧です \n
    ・species:ペンギンの種類（品種）\n 
            Adelie（アデリーペンギン）
            Chinstrap（ヒゲペンギン）
            Gentoo（ジェンツーペンギン）
                
    ・island:観測された島の名前 \n
            Torgersen（トルゲルセン島）
            Biscoe（ビスコー島）
            Dream（ドリーム島）
    ・bill_length_mm:クチバシの長さ（mm） \n
    ・bill_depth_mm:クチバシの厚さ・縦幅（mm） \n
    ・flipper_length_mm:フリッパー（翼・ひれ）の長さ（mm） \n
    ・body_mass_g:体重（グラム） \n
    ・sex:ペンギンの性別 \n


    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn penguinsデータ")
    

    ### データを表示
    if st.button('データを表示する',key='penguins_button' ):
        penguins = sns.load_dataset("penguins")
        st.dataframe(penguins)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('penguins')


    """,
        language="python",
    )

    st.write('\n \n ')
    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_penguins  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'],
        key='penguins_num_options'
    )

    #カテゴリーを選択
    category_options_penguins = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['species','island','sex'],
        key='penguins_category_options'
    )

    #統計量を決める
    statistic_penguins = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='penguins_statistic'
    )

    all_columns_penguins = ['species','island','bill_length_mm','bill_depth_mm',
                            'flipper_length_mm','body_mass_g','sex']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='penguins_stats_graph_button' ):
        penguins = sns.load_dataset("penguins")
        show_graph_and_table(category_options_penguins,num_options_penguins,
                             statistic_penguins,penguins,all_columns_penguins)


    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_penguins = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'],
        key='penguins_scatter_x'
    )
    #y軸指標を選択
    num_options_y_penguins = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'],
        key='penguins_scatter_y'
    )

    #カテゴリーを選択
    category_options_penguins = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['species','island','sex'],
        key='penguins_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='penguins_scatter_by_category_button' ):
        scatter_bycategory("penguins",num_options_x_penguins,num_options_y_penguins,category_options_penguins)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='penguins_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("penguins",num_options_x_penguins,num_options_y_penguins,category_options_penguins)


# planetsデータ (グラフ要検討)
with tab19:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
   planetsは太陽系外惑星（太陽以外の恒星の周りを回っている惑星）の発見に関する天文学のデータをまとめたものです。 \n
    
    
    
    \n\n\n
    以下変数一覧です \n
    ・method:惑星の発見方法（観測技術）\n 
                
    ・number:その恒星系で見つかっている惑星の数 \n
    ・orbital_period:公転周期（地球の日数換算） \n
    ・mass:惑星の質量（木星の質量を1とした比率） \n
    ・distance:地球（太陽系）からの距離（パーセク：pc単位） \n
    ・year:惑星が発見された西暦年 \n



    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn planetsデータ")
    

    ### データを表示
    if st.button('データを表示する',key='planets_button' ):
        planets = sns.load_dataset("planets")
        st.dataframe(planets)


    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('planets')


    """,
        language="python",
    )

    st.write('\n \n ')
    ### グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_planets  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['number','orbital_period','mass','distance','year'],
        key='planets_num_options'
    )

    #カテゴリーを選択
    category_options_planets = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['method'],
        key='planets_category_options'
    )

    #統計量を決める
    statistic_planets = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='planets_statistic'
    )

    all_columns_planets = ['number','orbital_period','mass','distance','year','method']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='planets_stats_graph_button' ):
        planets = sns.load_dataset("planets")
        show_graph_and_table(category_options_planets,num_options_planets,
                             statistic_planets,planets,all_columns_planets)


    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_planets = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['number','orbital_period','mass','distance','year'],
        key='planets_scatter_x'
    )
    #y軸指標を選択
    num_options_y_planets = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['number','orbital_period','mass','distance','year'],
        key='planets_scatter_y'
    )

    #カテゴリーを選択
    category_options_planets = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['method'],
        key='planets_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='planets_scatter_by_category_button' ):
        scatter_bycategory("planets",num_options_x_planets,num_options_y_planets,category_options_planets)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='planets_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("planets",num_options_x_planets,num_options_y_planets,category_options_planets)


# seaiceデータ (グラフ追加要検討)
with tab20:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    seaice（シーアイス）は、北極または地球全体の海氷面積（海に浮かぶ氷の広さ）の
    長期的な時系列データをまとめたデータセットです。 \n
    地球温暖化や気候変動の影響によって、世界の海氷が時代とともにどのように減少・変化しているかを
    可視化・分析するための教材としてよく使われます \n
    
    
    
    \n\n\n
    以下変数一覧です \n
    ・Date:観測された日付。フォーマットは YYYY-MM-DD（年-月-日）\n                 
    ・Extent:海氷面積（海氷域面積 / Sea Ice Extent）（$10^6\text{ km}^2$）\n

    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)
    

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn seaiceデータ")
    

    # データを表示
    if st.button('データを表示する',key='seaice_button' ):
        seaice = sns.load_dataset("seaice")
        st.dataframe(seaice)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('seaice')


    """,
        language="python",
    )

    st.write('\n \n ')
    # グラフを表示のサブヘッダー
    st.subheader("時系列のグラフを表示")
    if st.button('グラフを表示する',key='seaice_graph_button' ):
        time_series_graph("seaice","Date","Extent")

# taxisデータ (グラフ追加要検討)
with tab21:      
    #データの概要を説明
    st.subheader("データの概要")
    # 文章を挿入
    st.markdown('''
    taxis（タクシーズ）は、ニューヨーク市（NYC）におけるイエローキャブ（タクシー）およびグリーンキャブの乗車・運行記録データです。\n

    乗車・降車の日時や場所、走行距離といった運行データから、運賃、チップ、支払い方法などの金銭的なデータまで幅広く含まれており、
    データ分析、売上予測、GIS（地理情報システム）的な可視化、データクレンジングの練習に最適なデータセットです\n

    
    
    
    
    \n\n\n
    以下変数一覧です \n
    ・pickup:乗車日時\n  
    ・dropoff:降車日時\n                 
    ・passengers:乗客数\n
    ・distance:走行距離（マイル単位）\n
    ・fare:基本運賃（ドル）\n
    ・tip:チップ（ドル）\n
    ・tolls:有料道路・有料橋の通行料金（ドル）\n
    ・total:合計支払金額（ドル）\n
    ・color:タクシーの車体の色（種類）。\n
    ・payment:支払い方法\n
    ・pickup_zone:乗車した具体的なゾーン（地区）名\n
    ・dropoff_zone:降車した具体的なゾーン（地区）名\n
    ・pickup_borough:乗車した大地区（区/Borough）名\n
    ・dropoff_borough:降車した大地区（区/Borough）名\n

    \n \n \n
    <br><br>


    ''',unsafe_allow_html=True)
    

    # データを表示
    st.subheader("データを表示")

    # データを表示(今回はseabornのtipsデータを表示)
    st.write("seaborn taxisデータ")
    

    # データを表示
    if st.button('データを表示する',key='taxis_button' ):
        taxis = sns.load_dataset("taxis")
        st.dataframe(taxis)

    ### Pythonでのデータ読み込み方法
    st.write(" \n \n ")
    st.subheader("Pythonでのデータ読み込み方法")
    st.code(
    """
#seabornのモジュールをインポート
import seaborn as sns

#データをロード
df = sns.load_dataset('taxis')


    """,
        language="python",
    )

    st.write('\n \n ')
    # グラフを表示のサブヘッダー
    st.subheader("カテゴリごとの統計量を表示")


    #数値指標を選択
    num_options_taxis  = st.multiselect(
        '調べたい数値尺度を選択してください',
        ['passengers','distance','fare','tip','tolls','total'],
        key='taxis_num_options'
    )

    #カテゴリーを選択
    category_options_taxis = st.multiselect(
        '調べたいカテゴリ変数を選んでください',
        ['color','payment','pickup_zone','dropoff_zone','pickup_borough','dropoff_borough'],
        key='taxis_category_options'
    )

    #統計量を決める
    statistic_taxis = st.selectbox(
        '調べたい統計量を選んでください',
        static_list,
        key='taxis_statistic'
    )

    all_columns_taxis = ['pickup','dropoff','passengers','distance','fare',
                         'tip','tolls','total','color','payment','pickup_zone',
                         'dropoff_zone','pickup_borough','dropoff_borough']


    # グラフと表を表示
    if st.button('統計量とグラフを表示する',key='taxis_stats_graph_button' ):
        taxis = sns.load_dataset("taxis")
        show_graph_and_table(category_options_taxis,num_options_taxis,
                             statistic_taxis,taxis,all_columns_taxis)

    
    ### カテゴリーごとに散布図を表示
    st.write(" \n \n ")
    st.subheader("カテゴリー変数ごとに散布図を表示")
    #x軸指標を選択
    num_options_x_taxis = st.selectbox(
        '横軸に表示する数値尺度を選択してください',
        ['passengers','distance','fare','tip','tolls','total'],
        key='taxis_scatter_x'
    )
    #y軸指標を選択
    num_options_y_taxis = st.selectbox(
        '縦軸に表示する数値尺度を選択してください',
        ['passengers','distance','fare','tip','tolls','total'],
        key='taxis_scatter_y'
    )

    #カテゴリーを選択
    category_options_taxis = st.selectbox(
        '調べたいカテゴリ変数を選んでください',
        ['color','payment','pickup_borough','dropoff_borough'],
        key='taxis_scatter_category'
    )

    if st.button('カテゴリごとにグラフを分割して表示',key='taxis_scatter_by_category_button' ):
        scatter_bycategory("taxis",num_options_x_taxis,num_options_y_taxis,category_options_taxis)

    if st.button('カテゴリごとに色分けして1つのグラフに表示する',key='taxis_scatter_by_category_button_onegrapgh' ):
        scatter_bycategory_onegraph("taxis",num_options_x_taxis,num_options_y_taxis,category_options_taxis)
