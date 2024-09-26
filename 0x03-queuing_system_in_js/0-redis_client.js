#!/usr/bin/env node

import { createClient } from "redis";

/**
 * Initializes a Redis client and sets up event listeners to handle connection
 * status and errors.
 * 
 * The Redis client connects to the Redis server and logs a message when connected successfully.
 * If there is an error during connection, it logs an error message.
 * 
 * @constant {RedisClient}
 */

const client = createClient()
	
client
.on('error', (error) => console.error('Redis client not connected to the server:', error))
.on('connect', () => console.log('Redis client connected to the server'))
