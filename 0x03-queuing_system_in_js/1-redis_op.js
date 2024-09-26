#!/usr/bin/env node 

import { createClient, print } from "redis";

/**
 * Creates a Redis client for connecting to the Redis server.
 * 
 * The client is set up to handle connection events and errors.
 * 
 * @constant {RedisClient}
 */
const client = createClient()

client
.on('error', (error) => console.error('Redis client not connected to the server:', error))
.on('connect', () => console.log('Redis client connected to the server'))


/**
 * Sets a new value for a specified school in the Redis database.
 * 
 * This function uses the Redis SET command to store the value associated with the given school name.
 * 
 * @param {string} schoolName - The name of the school to set in the Redis database.
 * @param {string} value - The value to be associated with the school name.
 */
function setNewSchool(schoolName, value){
	client.SET(schoolName, value, print)
}


/**
 * Retrieves and displays the value associated with a specified school from the Redis database.
 * 
 * This function uses the Redis GET command to fetch the value for the given school name and logs it to the console.
 * 
 * @param {string} schoolName - The name of the school whose value is to be retrieved.
 */
function displaySchoolValue(schoolName){
	client.GET(schoolName, (error, reply) => {
		if (error){
			console.error(error)
		} else {
			console.log(reply)
		}
	})
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
