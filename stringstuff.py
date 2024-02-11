{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "19945de5",
   "metadata": {},
   "outputs": [],
   "source": [
    "mystring = \"abcdefghijk\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8e9f5854",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'abcdefghijk'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mystring"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3124e664",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'defghijk'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mystring[3:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5301d093",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'abcdefghijk'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mystring[::]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "adfd5a7b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'k'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mystring[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3d071b18",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'cdef'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mystring[2:6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8f13eec8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'kjihgfedcba'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mystring[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "46e13fba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'acegik'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mystring[::2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5dbc01a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "sum = int('2' + '3')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "116411fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "23"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "65964435",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'i', 'm', 'p', 's'}"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set('mississippi')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ba034f1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing jlgfile.txt\n"
     ]
    }
   ],
   "source": [
    "%%writefile jlgfile.txt\n",
    "this is my first jupyter file\n",
    "I have at least 2 lines\n",
    "Now I have 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "138e326d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/jerrygentry/Coding/100Days'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e58dbc1c",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'jlgfile' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/x5/q7c03c1x03x2gs36qnsgthpm0000gn/T/ipykernel_67385/1635202936.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mjlgfile\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'jlgfile' is not defined"
     ]
    }
   ],
   "source": [
    "jlgfile.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ef2cf1ff",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'jlgfilr' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/x5/q7c03c1x03x2gs36qnsgthpm0000gn/T/ipykernel_67385/2132255993.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mjlgfile\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mjlgfilr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtxt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'jlgfilr' is not defined"
     ]
    }
   ],
   "source": [
    "jlgfile = open(jlgfilr.txt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2b4ff7a4",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'jlgfile' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/x5/q7c03c1x03x2gs36qnsgthpm0000gn/T/ipykernel_67385/318993621.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mjlgfile\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mjlgfile\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtxt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'jlgfile' is not defined"
     ]
    }
   ],
   "source": [
    "jlgfile = open(jlgfile.txt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "37107f26",
   "metadata": {},
   "outputs": [],
   "source": [
    "jlgfile = open('jlgfile.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9ad6e5a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'this is my first jupyter file\\nI have at least 2 lines\\nNow I have 3\\n'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jlgfile.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "24c89856",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jlgfile.seek(0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "856aba47",
   "metadata": {},
   "outputs": [],
   "source": [
    "contents = jlgfile.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d1b71e8e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'this is my first jupyter file\\nI have at least 2 lines\\nNow I have 3\\n'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "contents"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "cb08fba7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jlgfile.seek(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5ee5b71a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['this is my first jupyter file\\n',\n",
       " 'I have at least 2 lines\\n',\n",
       " 'Now I have 3\\n']"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jlgfile.readlines()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5c4e0e10",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/jerrygentry/Coding/100Days'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "4896ef87",
   "metadata": {},
   "outputs": [],
   "source": [
    "jlgfile.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c74574a5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
