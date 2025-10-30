import pandas as pd
import xlsxwriter
import matplotlib.pyplot as plt


df = pd.read_csv('reward_debug.csv')
# with pd.ExcelWriter("debug_sheet.xlsx", engine='xlsxwriter') as writer:
#     df.to_excel(writer)

print(df.head())
plt.title('Reward entry over time')
plt.plot(df['reward_value'][:300], label='Reward')
plt.ylabel('Reward Value')
plt.xlabel('Time Step')
plt.show()

plt.title('x_position over time')
plt.plot(df['player_pos_x'][:300], label='X Position')
plt.ylabel('X Position')
plt.xlabel('Time Step')
plt.show()

# plt.title('x_position vs reward')
# plt.plot(df['player_pos_x'], df['reward_value'])
# plt.ylabel('Reward Value')
# plt.xlabel('X Position')
# plt.show()

