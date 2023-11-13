import streamlit as st
import mysql.connector

#establish connection  to my sql

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='testing'
)
mycursor=mydb.cursor()
print('vijay')

#create streamlit app
def main():
    st.title('book library')

    #display options for crud operations
    option=st.sidebar.selectbox('click here to record your book',('create book','update book','delete book'))
                                                
    #template to perform book details
    if option=="create book":
        st.subheader('enter book details')
        bookId=st.number_input('enter serial number',min_value=1)
        bookName=st.text_input('enter book name')
        book_cost=st.number_input('enter cost',min_value=1)
        if st.button('submit your book'):
            sql='insert into books(bookId,bookName,book_cost) values(%s,%s,%s)'
            val=(bookId,bookName,book_cost)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success('book submitted successfully')
          
    elif option=='delete book':
        st.subheader('delete your book')
        bookName=st.text_input('enter book name')
        if st.button('delete book'):
            sql='delete from books where bookName=%s'
            val=(bookName,)
            mycursor.execute(sql,val)
            mydb.commit()
            if bookName in sql:
                st.success('book Deleted successfully')
            else:
                 st.error('enter existed book name and try again:smile:')
        
            
    elif option=='update book':
        st.subheader('update your book')
        bookId=st.number_input('enter serial number',min_value=1)
        bookName=st.text_input('update book name')
        book_cost=st.number_input('update cost',min_value=1)
        if st.button('update book'):
            sql='update books set bookName=%s, book_cost= %s where bookId=%s'
            val=(bookId,bookName,book_cost)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success('updated successfully')

        
            
  
        

    
    





if __name__=='__main__':
    main()