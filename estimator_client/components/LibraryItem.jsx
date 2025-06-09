import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const LibraryItem = ({ item }) => (
    <View style={styles.libraryItem}>
        <Text style={styles.libraryName}>{item.name}</Text>
        <Text style={styles.libraryDescription}>{item.description}</Text>
    </View>
);

const styles = StyleSheet.create({
    libraryItem: {
        backgroundColor: '#f5f5f5',
        padding: 15,
        marginVertical: 5,
        borderRadius: 8,
    },
    libraryName: {
        fontSize: 16,
        fontWeight: 'bold',
    },
    libraryDescription: {
        fontSize: 14,
        color: '#666',
        marginTop: 4,
    }
});

export default LibraryItem;