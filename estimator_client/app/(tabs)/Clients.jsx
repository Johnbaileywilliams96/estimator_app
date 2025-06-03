import { router } from 'expo-router'
import React from 'react'
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native'


const app = () => {
  const handleLeadsPress = () => {
    router.push('/leads')
    console.log('Employees button pressed!')
    // Add your button logic here
  }

  const handleCustomerPress = () => {
    router.push('/customers')
  }



  return (
    <View style={styles.container}>
      <Text style={styles.text}>Business Name</Text>
      <TouchableOpacity style={styles.button} onPress={handleLeadsPress}>
        <Text style={styles.buttonText}>Leads</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button} onPress={handleCustomerPress}>
        <Text style={styles.buttonText}>Customer</Text>
      </TouchableOpacity>
    </View>
  )
}

export default app

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    color: 'grey',
    fontSize: 42,
    fontWeight: 'bold',
    textAlign: 'center'
  },
  button: {
    backgroundColor: '#007AFF',
    paddingHorizontal: 20,
    paddingVertical: 10,
    borderRadius: 8,
    marginTop: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
    textAlign: 'center'
  }
})