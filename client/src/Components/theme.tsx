import { View, Text, StyleSheet } from 'react-native';

const Card = ({ title, content }) => (
  <View style={styles.card}>
    <Text style={styles.title}>{title}</Text>
    <Text style={styles.content}>{content}</Text>
  </View>
);

const styles = StyleSheet.create({
  card: {
    padding: 16,
    backgroundColor: '#FFFFFF',
    borderRadius: 8,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#4A90E2', 
  },
  content: {
    fontSize: 14,
    color: '#333333',
  },
});

export default Card;