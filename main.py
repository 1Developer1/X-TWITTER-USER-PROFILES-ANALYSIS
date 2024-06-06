import networkx as nx
import json
from hash_Table import HashTable
from user1x import User
from interestedAnalyzer import InterestAnalyzer
from interestHashTable import InterestHashTable
from bfs import BFS
import matplotlib.pyplot as plt


def show_users(hash_table):
    print("=== Kullanıcılar ===")
    hash_table.display()


def search_user(hash_table):
    username = input("Aranacak Kullanıcı Adı: ")
    search_result = hash_table.ara(key=username)
    if search_result:
        print(f"Aranan Kullanıcı Bulundu: {search_result.username}")
    else:
        print("Kullanıcı Bulunamadı.")


def delete_user(hash_table):
    username = input("Silinecek Kullanıcı Adı: ")
    hash_table.sil(key=username)
    print("=== Son Durum ===")
    hash_table.display()


def match_users_by_interest(interest_hashTable):
    interest = input("Eşleştirilecek İlgi Alanı: ")
    interest_hashTable.match_users_selection_sort(interest)


def show_user_interests(interest_hashTable):
    username = input("Kullanıcı Adı: ")
    user_interests = interest_hashTable.get_user_interests(username)
    if user_interests:
        print(f"{username}'in ilgi alanları: {user_interests}")
    else:
        print(f"{username} kullanıcısı bulunamadı veya ilgi alanlarına sahip değil.")


def find_common_followers_bfs(G):
    username = input("Kullanıcı Adı: ")
    bfs_algo = BFS(G)
    result = bfs_algo.find_users_with_same_followers(username)
    print("BFS sonuç--->", result)


def draw_subgraph(G):
    username = input("Kullanıcı Adı: ")
    subgraph = nx.DiGraph()

    if username not in G.nodes:
        print("Kullanıcı bulunamadı!")
        return

    subgraph.add_node(username)

    for follower in G.predecessors(username):
        subgraph.add_edge(follower, username)

    for followed in G.successors(username):
        subgraph.add_edge(username, followed)

    pos = nx.spring_layout(subgraph)
    nx.draw(subgraph, pos, with_labels=True, node_color="skyblue", node_size=500, font_size=10, font_color="black",
            font_weight="bold", arrows=True)
    plt.title(f"{username}'ın İlişkileri")
    plt.show()


def save_to_txt(hash_table):
    with open("graph_representation.txt", "w", encoding="utf-8") as file:
        for username, user in hash_table:
            file.write(f"Düğüm: {username}\n")

            file.write("Giren Kenarlar (Takipçiler):\n")
            for follower in user.followers:
                file.write(follower + ",")

            file.write("\n")
            file.write("Çıkan Kenarlar (Takip Edilenler):\n")
            for following in user.following:
                file.write(following + ",")

            file.write("\n")

def save_to_txt(hash_table):
    with open("graph_representation.txt", "w", encoding="utf-8") as file:
        for username, user in hash_table:
            file.write(f"Düğüm: {username}\n")
            
            file.write("Giren Kenarlar (Takipçiler):\n")
            for follower in user.followers:
                file.write(follower +",")
            
            file.write("\n")
            file.write("Çıkan Kenarlar (Takip Edilenler):\n")
            for following in user.following:
                file.write(following +",")
            
            file.write("\n")



def main_menu():
    file_path = "C:\\Users\\XMG\\Desktop\\python\\ProLab3\\twitter_data.json"
    with open(file_path, "r", encoding="utf-8") as file:
        twitter_data = json.load(file)

    hash_table = HashTable(5)
    for user_data in twitter_data[:100]:
        user = User(user_data)
        hash_table.ekle(key=user.username, value=user)

    analyzer = InterestAnalyzer()
    interest_hashTable = InterestHashTable(analyzer.getInterestList())
    for username, user in hash_table:
        interest_hashTable.insert_user(user)

    G = nx.DiGraph()
    for username, user in hash_table:
        G.add_node(user.username)
        for follower in user.followers:
            G.add_edge(follower, user.username)
        for followed in user.following:
            G.add_edge(username, followed)

    while True:
        print("1. Kullanıcıları Göster")
        print("2. Kullanıcı Ara")
        print("3. Kullanıcı Sil")
        print("4. İlgi Alanlarına Göre Kullanıcı Eşleştir")
        print("5. Kullanıcı İlgi Alanlarını Göster")
        print("6. BFS ile Ortak Takipçilere Sahip Kullanıcıları Bul")
        print("7. Alt Grafik Çiz")
        print("8. Veriyi Dosyaya Kaydet")
        print("0. Çıkış")

        choice = input("Seçiminizi yapın (0-7): ")

        if choice == "1":
            show_users(hash_table)
        elif choice == "2":
            search_user(hash_table)
        elif choice == "3":
            delete_user(hash_table)
        elif choice == "4":
            match_users_by_interest(interest_hashTable)
        elif choice == "5":
            show_user_interests(interest_hashTable)
        elif choice == "6":
            find_common_followers_bfs(G)
        elif choice == "7":
            draw_subgraph(G)
        elif choice == "8":
            save_to_txt(hash_table)
            print("Veri başarıyla dosyaya kaydedildi.")
        elif choice == "0":
            break
        else:
            print("Geçersiz seçenek! Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main_menu()
