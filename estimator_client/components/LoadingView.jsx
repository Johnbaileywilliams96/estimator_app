import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const LoadingView = ({ message = "Loading..." }) => (
    <View style={styles.container}>
        <Text style={styles.text}>{message}</Text>
    </View>
);

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    text: {
        color: 'grey',
        fontSize: 42,
        fontWeight: 'bold',
        textAlign: 'center'
    }
});

export default LoadingView;