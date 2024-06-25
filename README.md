# GitHubアカウントの作成手順

### 1. GitHubのサイトにアクセス
まず、ウェブブラウザを開き、[GitHubの公式サイト](https://github.com/)にアクセスします。

### 2. サインアップページに移動
GitHubのトップページにアクセスしたら、右上の「Sign up」ボタンをクリックします。

### 3. アカウント情報の入力
サインアップページに移動したら、以下の情報を入力します。

- **Email address**: 使用するメールアドレスを入力します。
- **Password**: 安全なパスワードを設定します。パスワードは強力である必要があります。
- **Username**: ユーザー名を入力します。このユーザー名は他のユーザーと重複しないようにする必要があります。

### 4. パズルの解決
GitHubは、スパム防止のために簡単なパズルを解くように求めることがあります。指示に従ってパズルを解決してください。

### 5. メールアドレスの確認
入力したメールアドレスに確認メールが送信されます。メールを開き、確認リンクをクリックしてメールアドレスを確認します。

### 6. アカウントの設定
メールアドレスを確認した後、GitHubの初期設定を行います。以下の情報を入力します。

- **Team members**: チームメンバーの数を選択します。個人で使用する場合は「Just me」を選択します。
- **Role**: 学生や教師などの役割を選択します。

### 7. プランの選択
GitHubは無料プランと有料プランを提供しています。初めての場合は「GitHub Free」を選択し、「Continue for free」をクリックします。

### 8. ダッシュボードの確認
設定が完了すると、GitHubのダッシュボードに移動します。ここからリポジトリの作成や他のユーザーとのコラボレーションが可能になります。

これで、GitHubアカウントの作成が完了しました。GitHubを使ってプロジェクトを管理し、他の開発者とコラボレーションを始めましょう。

参考にした情報は以下の通りです：
- [GitHubの公式ドキュメント](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)[2]
- [AWS CodeDeployのチュートリアル](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-create-github-account.html)[1]

Citations:
[1] https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-create-github-account.html
[2] https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github
[3] https://www.youtube.com/watch?v=ohqfCGMP_zk
[4] https://www.youtube.com/watch?v=ldPuFlquiRk
[5] https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account
[6] https://www.youtube.com/watch?v=QUtk-Uuq9nE
[7] https://www.wikihow.com/Create-an-Account-on-GitHub
[8] https://docs.github.com/en/get-started/getting-started-with-git/set-up-git
[9] https://github.com/signup

# Template repository(このレポジトリ)から新しいリポジトリを作成する手順

1. GitHubにログインします。

2. 使用したいTemplate repositoryのページに移動します。

3. リポジトリ名の下にある緑色の「Use this template」ボタンをクリックします[1]。

4. ドロップダウンメニューから「Create a new repository」を選択します。

5. 新しいリポジトリの設定画面が表示されます。以下の項目を入力または選択します：

   - **Owner**: リポジトリの所有者を選択します（通常は自分のアカウント）。
   - **Repository name**: 新しいリポジトリの名前を入力します。
   - **Description**: リポジトリの説明を任意で入力します。
   - **Visibility**: パブリックまたはプライベートを選択します。
   - **Include all branches**: テンプレートの全ブランチを含めるかどうかを選択します（オプション）。

6. 設定が完了したら、「Create repository from template」ボタンをクリックします。

これで、選択したTemplate repositoryの内容を基に新しいリポジトリが作成されます。新しいリポジトリには、テンプレートのディレクトリ構造、ファイル、およびブランチ（選択した場合）がコピーされます[2]。

## Template repositoryを使用するメリット

- プロジェクトの初期設定時間を短縮できます。
- チーム内で一貫したプロジェクト構造を維持できます。
- よく使うボイラープレートコードや設定ファイルを簡単に再利用できます[2]。

Template repositoryを使用することで、プロジェクトの立ち上げがより迅速かつ効率的になります。特に、同じような構造のプロジェクトを頻繁に作成する場合や、チームで統一されたプロジェクト構造を維持したい場合に便利です。

Citations:
[1] https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
[2] https://gitprotect.io/blog/how-to-use-github-repository-templates/
[3] https://dev.to/dev_neil_a/how-to-create-and-use-github-repository-templates-4l06
[4] https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository
[5] https://docs.github.com/en/enterprise-cloud%40latest/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/setting-up-a-template-repository-for-github-codespaces
[6] https://stackoverflow.com/questions/62630485/is-it-possible-to-create-a-new-git-repository-from-a-template-only-using-the-com
[7] https://www.youtube.com/watch?v=3nm-DgqKE6I
[8] https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
[9] https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories
[10] https://qiita.com/ryo2132/items/08f0561804c798012146
[11] https://www.youtube.com/watch?v=8cxYgaMB9ow
[12] https://github.com/topics/template-repository


# データベース更新手順

0. 初期セットアップ（初回または環境再設定時のみ）
   - プロジェクトディレクトリに移動
   - OpenAI APIキーを環境変数に設定:
     ```
     export OPENAI_API_KEY='配ったものに書き換えてください'
     ```
   - 依存関係のインストールと仮想環境の作成:
     ```
     poetry install
     ```
   - Poetry シェルを起動して仮想環境に入る:
     ```
     poetry shell
     ```

1. Excelファイルの準備
   - 'text.xlsx' というファイル名で新しいExcelファイルを作成または既存のファイルを更新
   - ファイル内に 'text' という列を含める
   - 'text' 列に新しいドキュメントや更新したいテキストを入力

2. 既存のデータベースの削除
   - エクセルファイルを更新した場合、必ず既存の 'text.db' ファイルを削除してください
   - コマンドラインで以下を実行:
     ```
     rm text.db
     ```
   - または、ファイルエクスプローラーから 'text.db' ファイルを手動で削除

3. `excel_to_sqlite.py` スクリプトの実行
   - コマンドラインで以下を実行:
     ```
     python excel_to_sqlite.py
     ```
   - このスクリプトは以下の処理を行います:
     - Excelファイルを読み込む
     - 各テキストをOpenAIのAPIを使用してベクトル化
     - ベクトル化したデータを新しい `text.db` SQLiteデータベースに保存

4. アプリケーションの起動
   - コマンドラインで以下を実行してStreamlitアプリケーションを起動:
     ```
     streamlit run chat.py
     ```
   - これにより、新しいデータベースを使用したチャットボットアプリケーションが起動します
   - 起動後、ターミナルに以下のような情報が表示されます:
     ```
     Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.
     You can now view your Streamlit app in your browser.
     Local URL: http://localhost:8501
     Network URL: http://10.0.0.180:8501
     External URL: http://43.207.4.228:8501
     ```
   - External URL（例: http://43.207.4.228:8501）をクリックまたはブラウザにコピー＆ペーストして、アプリケーションにアクセスします

5. テスト
   - 起動したアプリケーションで、新しく追加したデータに関連する質問をして、正しく回答が得られることを確認

注意事項:
- OpenAI APIキーが正しく設定されていることを確認してください。セッションを閉じると環境変数がリセットされるため、新しいセッションを開始するたびにAPIキーを再設定する必要があります
- 大量のデータを一度に処理する場合は、APIの利用制限に注意してください
- データベースの更新前に重要なデータのバックアップを取ることをお勧めします
- エクセルファイルの更新と 'text.db' の削除を忘れると、古いデータと新しいデータが混在する可能性があります
- 仮想環境を終了するには、`exit` コマンドを使用してください
- 次回以降は、`poetry shell` コマンドで仮想環境に入ってから作業を開始してください
- External URLは環境によって異なる場合があります。表示されたURLを使用してください