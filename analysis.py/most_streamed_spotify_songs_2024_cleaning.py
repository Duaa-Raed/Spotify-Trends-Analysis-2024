
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




# Display first 10 rows
print("\nFirst 10 rows of the dataset:")
print(most_Streamed_Spotify_Songs_2024.head(10))

# Display dataset info
print("\nDataset Information:")
print(most_Streamed_Spotify_Songs_2024.info())

# تحويل "Explicit Track" إلى عدد صحيح
most_Streamed_Spotify_Songs_2024['Explicit Track'] = most_Streamed_Spotify_Songs_2024['Explicit Track'].astype(int)

# تحويل "Release Date" إلى تاريخ
most_Streamed_Spotify_Songs_2024['Release Date'] = pd.to_datetime(most_Streamed_Spotify_Songs_2024['Release Date'], errors='coerce')

# الأعمدة التي لا نريد تحويلها
exclude_columns = ['Track', 'Album Name', 'Artist', 'Release Date', 'ISRC', 'TIDAL Popularity', 'Explicit Track']

# تحويل باقي الأعمدة الرقمية
for column in most_Streamed_Spotify_Songs_2024.columns:
    if column not in exclude_columns:
        most_Streamed_Spotify_Songs_2024[column] = (
            most_Streamed_Spotify_Songs_2024[column]
            .astype(str)
            .str.replace(',', '', regex=False)
        )
        most_Streamed_Spotify_Songs_2024[column] = pd.to_numeric(most_Streamed_Spotify_Songs_2024[column], errors='coerce')

# حذف أعمدة غير مفيدة
most_Streamed_Spotify_Songs_2024 = most_Streamed_Spotify_Songs_2024.drop(['ISRC', 'TIDAL Popularity'], axis=1)

# طباعة المعلومات والملخص
print("\n✅ Updated Dataset Information:")
print(most_Streamed_Spotify_Songs_2024.info())

print("\n📊 Statistical Description:")
print(most_Streamed_Spotify_Songs_2024.describe())

print("\n🧾 Column Names:")
print(most_Streamed_Spotify_Songs_2024.columns)

# دالة لتحويل الأرقام إلى صيغة مليون/مليار
def format_number(x, pos):
    if x >= 1e9:
        return f'{x/1e9:.1f}B'
    elif x >= 1e6:
        return f'{x/1e6:.0f}M'
    else:
        return f'{x:.0f}'

# حساب معامل الارتباط بين Spotify Streams و YouTube Views
correlation = most_Streamed_Spotify_Songs_2024['Spotify Streams'].corr(most_Streamed_Spotify_Songs_2024['YouTube Views'])
print("\n📊 Correlation between Spotify Streams and YouTube Views:", correlation)

# رسم Scatter Plot مع خط الانحدار
plt.figure(figsize=(10, 6))
sns.regplot(data=most_Streamed_Spotify_Songs_2024, 
            x='Spotify Streams', 
            y='YouTube Views',
            scatter_kws={'alpha':0.5},
            line_kws={'color': 'red'})

# تطبيق التنسيق الجديد على المحاور
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_number))
ax.yaxis.set_major_formatter(plt.FuncFormatter(format_number))

plt.xlabel('Spotify Streams')
plt.ylabel('YouTube Views')
plt.title(f'Relationship between Spotify Streams and YouTube Views\nCorrelation: {correlation:.2f}')
plt.grid(True, alpha=0.3)
plt.show()

# حساب معامل الارتباط بين Spotify Streams و TikTok Posts
correlation_tiktok = most_Streamed_Spotify_Songs_2024['Spotify Streams'].corr(most_Streamed_Spotify_Songs_2024['TikTok Posts'])
print("\n📊 Correlation between Spotify Streams and TikTok Posts:", correlation_tiktok)

# رسم Scatter Plot مع خط الانحدار للعلاقة بين Spotify Streams و TikTok Posts
plt.figure(figsize=(10, 6))
sns.regplot(data=most_Streamed_Spotify_Songs_2024, 
            x='Spotify Streams', 
            y='TikTok Posts',
            scatter_kws={'alpha':0.5},
            line_kws={'color': 'red'})

# تطبيق التنسيق الجديد على المحاور
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_number))
ax.yaxis.set_major_formatter(plt.FuncFormatter(format_number))

plt.xlabel('Spotify Streams')
plt.ylabel('TikTok Posts')
plt.title(f'Relationship between Spotify Streams and TikTok Posts\nCorrelation: {correlation_tiktok:.2f}')
plt.grid(True, alpha=0.3)
plt.show()

# حساب معامل الارتباط بين YouTube Views و YouTube Likes
correlation_yt = most_Streamed_Spotify_Songs_2024['YouTube Views'].corr(most_Streamed_Spotify_Songs_2024['YouTube Likes'])
print("\n📊 Correlation between YouTube Views and YouTube Likes:", correlation_yt)

# رسم Scatter Plot مع خط الانحدار للعلاقة بين YouTube Views و YouTube Likes
plt.figure(figsize=(10, 6))
sns.regplot(data=most_Streamed_Spotify_Songs_2024, 
            x='YouTube Views', 
            y='YouTube Likes',
            scatter_kws={'alpha':0.5},
            line_kws={'color': 'red'})

# تطبيق التنسيق الجديد على المحاور
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_number))
ax.yaxis.set_major_formatter(plt.FuncFormatter(format_number))

plt.xlabel('YouTube Views')
plt.ylabel('YouTube Likes')
plt.title(f'Relationship between YouTube Views and YouTube Likes\nCorrelation: {correlation_yt:.2f}')
plt.grid(True, alpha=0.3)
plt.show()

# رسم Box Plot للعلاقة بين Spotify Streams و Explicit Track
plt.figure(figsize=(10, 6))
sns.boxplot(data=most_Streamed_Spotify_Songs_2024,
            x='Explicit Track',
            y='Spotify Streams')

# تطبيق التنسيق على المحور Y
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(format_number))

plt.xlabel('Explicit Track')
plt.ylabel('Spotify Streams')
plt.title('Distribution of Spotify Streams by Explicit Track Status')
plt.grid(True, alpha=0.3)
plt.show()

# تحليل إحصائي للـ Spotify Streams حسب Explicit Track
streams_by_explicit = most_Streamed_Spotify_Songs_2024.groupby('Explicit Track')['Spotify Streams'].describe()
streams_by_explicit = streams_by_explicit.round(2)

print("\n📊 Statistical Analysis of Spotify Streams by Explicit Track Status:")
print("\nDetailed statistical description:")
print(streams_by_explicit)

# حساب النسبة المئوية للأغاني حسب Explicit Track
explicit_percentage = (most_Streamed_Spotify_Songs_2024['Explicit Track'].value_counts() / len(most_Streamed_Spotify_Songs_2024) * 100).round(2)
print("\nPercentage of tracks by Explicit status:")
print(explicit_percentage)

# إضافة عمود جديد يحتوي على سنة الإصدار
most_Streamed_Spotify_Songs_2024['Release Year'] = most_Streamed_Spotify_Songs_2024['Release Date'].dt.year

# عرض توزيع الأغاني حسب سنة الإصدار
print("\n📅 Distribution of tracks by Release Year:")
year_distribution = most_Streamed_Spotify_Songs_2024['Release Year'].value_counts().sort_index()
print(year_distribution)


# تحليل إحصائي حسب سنة الإصدار باستخدام describe()
yearly_stats = most_Streamed_Spotify_Songs_2024.groupby('Release Year')['Spotify Streams'].describe()
print("\n📊 Statistical Analysis by Release Year:")
print(yearly_stats)
# رسم بياني للعلاقة بين سنة الإصدار وعدد الاستماع على Spotify
plt.figure(figsize=(12, 6))
sns.boxplot(data=most_Streamed_Spotify_Songs_2024,
            x='Release Year',
            y='Spotify Streams')

# تطبيق التنسيق على المحور Y
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(format_number))

plt.xticks(rotation=45)
plt.xlabel('Release Year')
plt.ylabel('Spotify Streams')
plt.title('Distribution of Spotify Streams by Release Year')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# تحديد المسار لحفظ الرسوم البيانية
output_path = "C:/Users/duaar/OneDrive/Desktop/Images"

# إعادة إنشاء وحفظ الرسم البياني الأول (توزيع عدد الاستماع حسب Explicit Track)
plt.figure(figsize=(10, 6))
sns.boxplot(data=most_Streamed_Spotify_Songs_2024, 
            x='Explicit Track', 
            y='Spotify Streams')
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(format_number))
plt.xlabel('Explicit Track')
plt.ylabel('Spotify Streams')
plt.title('Distribution of Spotify Streams by Explicit Track Status')
plt.grid(True, alpha=0.3)
plt.savefig(f"{output_path}/streams_by_explicit.png", bbox_inches='tight', dpi=300)
plt.close()

# إعادة إنشاء وحفظ الرسم البياني الثاني (توزيع عدد الاستماع حسب سنة الإصدار)
plt.figure(figsize=(12, 6))
sns.boxplot(data=most_Streamed_Spotify_Songs_2024,
            x='Release Year',
            y='Spotify Streams')
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(format_number))
plt.xticks(rotation=45)
plt.xlabel('Release Year')
plt.ylabel('Spotify Streams')
plt.title('Distribution of Spotify Streams by Release Year')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_path}/streams_by_year.png", bbox_inches='tight', dpi=300)
plt.close()

print("\n✅ تم حفظ الرسوم البيانية في المجلد:", output_path)

















