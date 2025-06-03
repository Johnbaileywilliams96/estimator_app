import React from 'react'
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native'

const app = () => {
  const handleEmployeesPress = () => {
    console.log('Employees button pressed!')
    // Add your button logic here
  }

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Business Name</Text>
      <TouchableOpacity style={styles.button} onPress={handleEmployeesPress}>
        <Text style={styles.buttonText}>Employees</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button} onPress={handleEmployeesPress}>
        <Text style={styles.buttonText}>Business Profile</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button} onPress={handleEmployeesPress}>
        <Text style={styles.buttonText}>Customers</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button} onPress={handleEmployeesPress}>
        <Text style={styles.buttonText}>Business Contracts</Text>
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